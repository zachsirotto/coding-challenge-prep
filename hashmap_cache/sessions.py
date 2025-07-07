from typing import Optional
from dataclasses import dataclass
from collections import defaultdict



@dataclass
class Session:
  user_id: str
  start_time: int
  duration: int

  def is_active_at(self, ts: int) -> bool:
    return self.start_time <= ts < self.start_time + self.duration


@dataclass
class Entry:
  op: OperationType
  ts: int
  args: tuple

class SessionTracker:
  def __init__(self):
    self.sessions = {}
    self.user_sessions = defaultdict(list)
    self.log = []
    self.timeline = defaultdict(int)
    self.peak_concurrent = 0
    

  # LEVEL 1

  def start_session(self, user_id: str, start_time: int, duration: int):
    """
    Start a new session for the given user.
    Raise RuntimeError if a session already exists for the same user at the same start time.
    """
    key = (user_id, start_time)
    if key in self.sessions:
      raise RuntimeError(f'Session for "{user_id}" at "{start_time}" already exists')
    session = Session(user_id, start_time, duration)
    self.sessions[key] = session
    self.user_sessions[user_id].append(session)


  def get_session_duration(self, user_id: str, start_time: int) -> Optional[int]:
    """
    Return the duration of the given session if it exists, or None.
    """
    session = self.sessions.get((user_id, start_time))
    if not session:
      return None
    return session.duration

  # LEVEL 2
  def get_active_users_at(self, ts: int) -> list[str]:
    """
    Return all users who have an active session at a given timestamp.
    """
    users = set()
    for (user_id, start_time), session in self.sessions.items():
      if session.is_active_at(ts):
        users.add(session.user_id)
    return list(sorted(users))


  def get_total_session_time(self, user_id: str) -> int:
    """
    Sum the durations of all sessions for a given user.
    """
    return sum(s.duration for s in self.user_sessions.get(user_id))

  # LEVEL 3
  def _get_session(self, user_id: str, start_time: int):
    key = (user_id, start_time)
    if key not in self.sessions:
      raise RuntimeError(f'Session for "{user_id}" at "{start_time}" not found')
    return self.sessions.get(key)

  def extend_session(self, user_id, start_time, additional_time):
    """
    Extend a session by a given amount of additional time.
    """
    session = self._get_session(user_id, start_time)
    session.duration += additional_time

  def end_session_early(self, user_id, start_time, end_time):
    """
    End a session early at a specific end time.
    """
    session = self._get_session(user_id, start_time)
    old_end_time = session.start_time + session.duration
    if end_time < session.start_time:
      raise RuntimeError('Session end time cannot come before session start time')
    session.duration = min(end_time - session.start_time, session.duration)

  def rollback(self, ts: int) -> None:
    """
    Revert the system to the state it was in at the given timestamp.
    """
    self.sessions.clear()
    self.user_sessions.clear()
    self.timeline.clear()
