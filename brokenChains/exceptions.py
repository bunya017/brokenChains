from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status



class UniqueTogetherValidationError(APIException):
	status_code = status.HTTP_403_FORBIDDEN
	default_detail = '403 Forbidden.'

	def __init__(self, detail, field, status_code):
		if status_code is not None:
			self.status_code = status_code
		if detail is not None:
			self.detail = {field: force_text(detail)}
		else:
			self.detail = {'detail': force_text(self.default_detail)}


class RaiseCustomError(APIException):
	status_code = status.HTTP_404_NOT_FOUND
	default_detail = '404 Not Found.'

	def __init__(self, detail, status_code):
		if status_code is not None:
			self.status_code = status_code
		if detail is not None:
			self.detail = {'detail': force_text(detail)}
		else:
			self.detail = {'detail': force_text(self.default_detail)}