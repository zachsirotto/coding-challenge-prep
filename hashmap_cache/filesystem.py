from typing import Optional, Dict, List
from dataclasses import dataclass
import time


@dataclass
class FileAction:
  type: str
  args: tuple
  ts: int

@dataclass
class File:
  name: str
  size: int
  created_at: int
  ttl: Optional[int]

  def is_alive(self, now: int) -> bool:
    if self.ttl is None:
      return True
    return now < self.created_at + self.ttl

class FileSystem:
  def __init__(self):
    self.memory: Dict[str, File] = {}
    self.history: List[FileAction] = []

  def file_upload_at(self, ts: int, filename: str, size: int, ttl: Optional[int] = None):
    if filename in self.memory:
      raise RuntimeError(f'Filename "{filename}" already exists in memory')
    self.memory[filename] = File(filename, size, ts, ttl)
    self.history.append(FileAction("upload", (filename, size, ts, ttl), ts))

  def file_get_at(self, ts: int, file_name: str) -> Optional[int]:
    file = self.memory.get(file_name)
    if file and file.is_alive(ts):
      return file.size
    return None

  def file_copy_at(self, ts: int, source: str, dest: str) -> None:
    if source not in self.memory:
      raise RuntimeError(f'Source "{source}" doesn\'t exist')
    f = self.memory[source]
    if f.is_alive(ts):
      # overwrite file
      self.memory[dest] = File(dest, f.size, ts, f.ttl)
      self.history.append(FileAction("copy", (source, dest, ts), ts))

  def file_search_at(self, ts: int, prefix: str) -> list[str]:
    result = [f for f in self.memory if f.startswith(prefix) and self.memory[f].is_alive(ts)]
    result.sort(key=lambda f: (-self.memory[f].size, f))
    return result[:10]


  def rollback(self, rollback_ts: int) -> None:
    """
    Reverts the system to how it looked at a specific timestamp.
    """
    self.memory: Dict[str, File] = {}

    for action in self.history:
      # skip actions that are after rollback time
      if action.ts > rollback_ts:
        continue

      if action.type == "upload":
        name, sz, created_at, ttl = action.args
        if created_at <= rollback_ts:
          f = File(name, sz, created_at, ttl)
          if f.is_alive(rollback_ts):
            self.memory[name] = f
      elif action.type == "copy":
        source, dest, ts = action.args
        source_file = self.memory.get(source)
        if source_file and source_file.is_alive(rollback_ts):
          if source_file.ttl is not None:
            expiry = source_file.created_at + source_file.ttl
            ttl_remaining = max(expiry - rollback_ts, 0)
          else:
            ttl_remaining = None
          f = File(dest, source_file.size, ts, ttl_remaining)
          if f.is_alive(rollback_ts):
            self.memory[dest] = f
