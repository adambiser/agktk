from appgamekit import (
    # Multiplayer > UDP
    create_udp_listener as _create_udp_listener,
    delete_udp_listener as _delete_udp_listener,
    get_udp_network_message as _get_udp_network_message,
    send_udp_network_message as _send_udp_network_message,
    # Multiplayer > Setup
    close_network as _close_network,
    # get_network_exists,  # Not needed
    host_network as _host_network,
    is_network_active as _is_network_active,
    join_network as _join_network,
    set_network_allow_clients as _set_network_allow_clients,
    set_network_latency as _set_network_latency,
    set_network_no_more_clients as _set_network_no_more_clients,
    # Multiplayer > Properties
    delete_network_client as _delete_network_client,
    # get_device_ip,  # See device module.
    # get_device_ipv6,  # See device module.
    get_network_client_disconnected as _get_network_client_disconnected,
    get_network_client_float as _get_network_client_float,
    get_network_client_ip as _get_network_client_ip,
    get_network_client_integer as _get_network_client_integer,
    get_network_client_name as _get_network_client_name,
    get_network_client_ping as _get_network_client_ping,
    get_network_client_user_data as _get_network_client_user_data,
    get_network_first_client as _get_network_first_client,
    get_network_my_client_id as _get_network_my_client_id,
    get_network_next_client as _get_network_next_client,
    get_network_num_clients as _get_network_num_clients,
    get_network_server_id as _get_network_server_id,
    get_network_server_ip as _get_network_server_ip,
    kick_network_client as _kick_network_client,
    set_network_client_user_data as _set_network_client_user_data,
    set_network_local_float as _set_network_local_float,
    set_network_local_integer as _set_network_local_integer,
    # Multiplayer > Broadcast
    create_broadcast_listener as _create_broadcast_listener,
    delete_broadcast_listener as _delete_broadcast_listener,
    get_broadcast_message as _get_broadcast_message,
    # Multiplayer > Sockets
    connect_socket as _connect_socket,
    delete_socket as _delete_socket,
    flush_socket as _flush_socket,
    get_socket_byte as _get_socket_byte,
    get_socket_bytes_available as _get_socket_bytes_available,
    get_socket_connected as _get_socket_connected,
    # get_socket_exists,  # Not needed.
    get_socket_float as _get_socket_float,
    get_socket_integer as _get_socket_integer,
    get_socket_remote_ip as _get_socket_remote_ip,
    get_socket_string as _get_socket_string,
    send_socket_byte as _send_socket_byte,
    send_socket_float as _send_socket_float,
    send_socket_integer as _send_socket_integer,
    send_socket_string as _send_socket_string,
    # Multiplayer > Messages
    add_network_message_byte as _add_network_message_byte,
    add_network_message_float as _add_network_message_float,
    add_network_message_integer as _add_network_message_integer,
    add_network_message_string as _add_network_message_string,
    copy_network_message as _copy_network_message,
    create_network_message as _create_network_message,
    delete_network_message as _delete_network_message,
    get_network_message as _get_network_message,
    get_network_message_byte as _get_network_message_byte,
    get_network_message_float as _get_network_message_float,
    get_network_message_from_client as _get_network_message_from_client,
    get_network_message_from_ip as _get_network_message_from_ip,
    get_network_message_from_port as _get_network_message_from_port,
    get_network_message_integer as _get_network_message_integer,
    get_network_message_string as _get_network_message_string,
    send_network_message as _send_network_message,
    # Multiplayer > Socket Listener
    create_socket_listener as _create_socket_listener,
    delete_socket_listener as _delete_socket_listener,
    get_socket_listener_connection as _get_socket_listener_connection,
)
from ._enums import SocketState, VariableType
from typing import List


class NetworkMessage(object):
    """
    Wraps AppGameKit network message methods.
    """
    def __init__(self):
        self.__id = _create_network_message()

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_network_message(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def add_byte(self, value: int):
        _add_network_message_byte(self.__id, value)

    def add_float(self, value: float):
        _add_network_message_float(self.__id, value)

    def add_integer(self, value: int):
        _add_network_message_integer(self.__id, value)

    def add_string(self, value: str):
        _add_network_message_string(self.__id, value)

    @classmethod
    def _from_id(cls, message_id):
        if not message_id:
            return None
        msg = cls.__new__(cls)
        msg.__id = message_id
        return msg

    def copy(self) -> "NetworkMessage":
        return NetworkMessage._from_id(_copy_network_message(self.__id))

    def get_byte(self) -> int:
        return _get_network_message_byte(self.__id)

    def get_float(self) -> float:
        return _get_network_message_float(self.__id)

    def get_integer(self) -> int:
        return _get_network_message_integer(self.__id)

    def get_string(self) -> str:
        return _get_network_message_string(self.__id)

    @property
    def from_client(self) -> int:
        return _get_network_message_from_client(self.__id)

    @property
    def from_ip(self) -> str:
        return _get_network_message_from_ip(self.__id)

    @property
    def from_port(self) -> int:
        return _get_network_message_from_port(self.__id)


class UdpListener(object):
    """
    Wraps AppGameKit UDP Listener methods.
    """
    def __init__(self, ip: str, port: int):
        self.__id = _create_udp_listener(ip, port)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_udp_listener(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def get_message(self):
        # noinspection PyProtectedMember
        return NetworkMessage._from_id(_get_udp_network_message(self.__id))

    def send_message(self, message: NetworkMessage, ip: str, port: int):
        _send_udp_network_message(self.__id, message.id, ip, port)


class NetworkClient(object):
    """
    Wraps AppGameKit network client methods.
    """
    def __init__(self, network_id: int, client_id: int):
        self.__network_id = network_id
        self.__id = client_id

    def __del__(self):
        """Deletes the object."""
        try:
            _close_network(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def ip(self) -> str:
        return _get_network_client_ip(self.__network_id, self.__id)

    @property
    def name(self) -> str:
        return _get_network_client_name(self.__network_id, self.__id)

    @property
    def ping(self) -> float:
        return _get_network_client_ping(self.__network_id, self.__id)

    @property
    def is_disconnected(self) -> bool:
        return _get_network_client_disconnected(self.__network_id, self.__id)

    @property
    def is_me(self) -> bool:
        return self.__id == _get_network_my_client_id(self.__network_id)

    @property
    def is_server(self) -> bool:
        return self.__id == _get_network_server_id(self.__network_id)

    def delete(self):
        _delete_network_client(self.__network_id, self.__id)

    def kick(self):
        _kick_network_client(self.__network_id, self.__id)

    def get_float(self, name: str) -> float:
        return _get_network_client_float(self.__network_id, self.__id, name)

    def get_integer(self, name: str) -> int:
        return _get_network_client_integer(self.__network_id, self.__id, name)

    def get_user_data(self, slot: int) -> int:
        return _get_network_client_user_data(self.__network_id, self.__id, slot)

    def set_user_data(self, slot: int, value: int):
        _set_network_client_user_data(self.__network_id, self.__id, slot, value)

    def send_message(self, message: NetworkMessage):
        _send_network_message(self.__network_id, self.__id, message.id)


class Network(object):
    """
    Wraps AppGameKit network methods.
    """
    def __init__(self, network_name: str, my_name: str, port: int, portv6: int = 0):
        self.__id = _host_network(network_name, my_name, port, portv6)

    def __del__(self):
        """Deletes the object."""
        try:
            _close_network(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def is_active(self) -> bool:
        return _is_network_active(self.__id)

    @property
    def my_client(self) -> NetworkClient:
        _id = self.__id
        return NetworkClient(_id, _get_network_my_client_id(_id))

    @property
    def server_client(self) -> NetworkClient:
        _id = self.__id
        return NetworkClient(_id, _get_network_server_id(_id))

    @property
    def server_ip(self) -> str:
        return _get_network_server_ip(self.__id)

    @classmethod
    def join(cls, network_name: str, my_name: str):
        n = cls.__new__(cls)
        n.__id = _join_network(network_name, my_name)

    def set_latency(self, latency: int):
        _set_network_latency(self.__id, latency)

    def set_allow_clients(self, enabled: bool):
        if enabled:
            _set_network_allow_clients(self.__id)
        else:
            _set_network_no_more_clients(self.__id)

    def set_local_float(self, name: str, value: float, mode: VariableType = VariableType.NORMAL):
        _set_network_local_float(self.__id, name, value, mode)

    def set_local_integer(self, name: str, value: int, mode: VariableType = VariableType.NORMAL):
        _set_network_local_integer(self.__id, name, value, mode)

    @property
    def client_count(self) -> int:
        return _get_network_num_clients(self.__id)

    @property
    def clients(self) -> List[NetworkClient]:
        # All clients must be read at once or the internal network code can't continue processing.
        network_id = self.__id

        def get_client_ids():
            client_id = _get_network_first_client(network_id)
            while client_id:
                yield client_id
                client_id = _get_network_next_client(network_id)

        return [NetworkClient(network_id, client_id) for client_id in get_client_ids()]

    def get_message(self) -> NetworkMessage:
        # noinspection PyProtectedMember
        return NetworkMessage._from_id(_get_network_message(self.__id))


class BroadcastListener(object):
    """
    Wraps AppGameKit broadcast listener methods.
    """
    def __init__(self, port: int):
        self.__id = _create_broadcast_listener(port)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_broadcast_listener(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def get_message(self) -> NetworkMessage:
        # noinspection PyProtectedMember
        return NetworkMessage._from_id(_get_broadcast_message(self.__id))


class Socket(object):
    """
    Wraps AppGameKit socket methods.
    """
    def __init__(self, ip: str, port: int, timeout: int = 3000):
        self.__id = _connect_socket(ip, port, timeout)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_socket(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def state(self) -> SocketState:
        return SocketState(_get_socket_connected(self.__id))

    @property
    def remote_ip(self) -> str:
        return _get_socket_remote_ip(self.__id)

    def flush(self):
        _flush_socket(self.__id)

    def get_bytes_available(self):
        return _get_socket_bytes_available(self.__id)

    def get_byte(self) -> int:
        return _get_socket_byte(self.__id)

    def get_float(self) -> float:
        return _get_socket_float(self.__id)

    def get_integer(self) -> int:
        return _get_socket_integer(self.__id)

    def get_string(self) -> str:
        return _get_socket_string(self.__id)

    def send_byte(self, value: int):
        _send_socket_byte(self.__id, value)

    def send_float(self, value: float):
        _send_socket_float(self.__id, value)

    def send_integer(self, value: int):
        _send_socket_integer(self.__id, value)

    def send_string(self, value: str):
        _send_socket_string(self.__id, value)


class SocketListener(object):
    """
    Wraps AppGameKit socket listener methods.
    """
    def __init__(self, ip: str, port: int):
        self.__id = _create_socket_listener(ip, port)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_socket_listener(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def get_connections(self):
        while True:
            socket_id = _get_socket_listener_connection(self.__id)
            if not socket_id:
                break
            socket = Socket.__new__(Socket)
            socket.__id = socket_id
            yield socket
