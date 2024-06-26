
from rest_framework.throttling import UserRateThrottle

class JackThrottle(UserRateThrottle):
  scope = 'jack'