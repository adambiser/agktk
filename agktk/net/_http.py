"""
Contains HTTP connection functionality.
"""

# noinspection PyUnresolvedReferences
from appgamekit import (
    # HTTP > General
    add_http_header as _add_http_header,
    close_http_connection as _close_http_connection,
    create_http_connection as _create_http_connection,
    delete_http_connection as _delete_http_connection,
    get_http_file as _get_http_file,
    # get_http_file_complete,  # Not needed.  Doesn't do anything get_http_response_ready doesn't do.
    get_http_file_progress as _get_http_file_progress,
    get_http_response as _get_http_response,
    get_http_response_ready as _get_http_response_ready,
    get_http_status_code as _get_http_status_code,
    # get_internet_state,  # See device
    # open_browser,  # See device
    remove_http_header as _remove_http_header,
    send_http_file as _send_http_file,
    send_http_request as _send_http_request,
    send_http_request_async as _send_http_request_async,
    set_http_host as _set_http_host,
    set_http_timeout as _set_http_timeout,
    set_http_verify_certificate as _set_http_verify_certificate,
)
from agktk._enums import HttpResponseState


class HttpConnection(object):
    """Wraps HTTP connection functionality."""
    def __init__(self, host: str, secure: bool = False, username: str = None, password: str = None):
        self.__id = _create_http_connection()
        if host:
            if not self.set_host(host, secure, username, password):
                raise RuntimeWarning(f"Could not connect to host: {host}")

    def __del__(self):
        """Delete the object."""
        try:
            # This closes the connection internally.
            _delete_http_connection(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self):
        return self.__id

    @classmethod
    def build_url_parameters(cls, parameters) -> str:
        try:
            # Is parameters a dict[str, str]?
            return "&".join([f"{url_encode(key)}={url_encode(value)}" for key, value in parameters.items()])
        except AttributeError:
            pass
        # Must be Iterable[Tuple[str, str]].
        return "&".join([f"{url_encode(key)}={url_encode(value)}" for key, value in parameters])

    def set_host(self, host: str, secure: bool = False, username: str = None, password: str = None) -> bool:
        return _set_http_host(self.__id, host, secure, username, password)

    def set_timeout(self, milliseconds: int):
        _set_http_timeout(self.__id, milliseconds)

    def enable_certificate_verification(self, enabled: bool):
        _set_http_verify_certificate(self.__id, enabled)

    def add_header(self, name: str, value: str):
        _add_http_header(self.__id, name, value)

    def remove_header(self, name: str):
        _remove_http_header(self.__id, name)

    def close(self):
        _close_http_connection(self.__id)

    def get_file_async(self, server_filename: str, local_filename: str, post_data: str = None) -> bool:
        return _get_http_file(self.__id, server_filename, local_filename, post_data)

    # _get_http_file_complete seems to be the same as get_http_response_ready.  Just use it.
    # def get_file_state(self) -> HttpResponseState:
    #     if _get_http_file_complete(self.__id):
    #         return HttpResponseState(_get_http_response_ready(self.__id))
    #     return HttpResponseState.IN_PROGRESS

    @property
    def file_progress(self) -> float:
        return _get_http_file_progress(self.__id)

    @property
    def response(self) -> str:
        return _get_http_response(self.__id)

    @property
    def response_state(self) -> HttpResponseState:
        return HttpResponseState(_get_http_response_ready(self.__id))

    @property
    def status_code(self) -> int:
        return _get_http_status_code(self.__id)

    def send_file_async(self, server_filename: str, post_data: str, local_filename: str) -> bool:
        return _send_http_file(self.__id, server_filename, post_data, local_filename)

    def send_request(self, server_filename: str, post_data: str = None) -> str:
        return _send_http_request(self.__id, server_filename, post_data)

    def send_request_async(self, server_filename: str, post_data: str = None) -> bool:
        return _send_http_request_async(self.__id, server_filename, post_data)
