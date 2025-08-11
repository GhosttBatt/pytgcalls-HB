# from ntgcalls import DeviceInfo as RawDeviceInfo

try:
    from ntgcalls import DeviceInfo as RawDeviceInfo
except ImportError:
    RawDeviceInfo = None  # Fallback if DeviceInfo doesn't exist

from ntgcalls import NTgCalls

from ..types.list import List
from .input_device import InputDevice
from .screen_device import ScreenDevice
from .speaker_device import SpeakerDevice


class MediaDevices:
    @staticmethod
    def _parse_devices(devices: list, is_video: bool) -> List:
        return List(
            InputDevice(device.name, device.metadata, is_video)
            for device in devices
        )

    @staticmethod
    def microphone_devices() -> List:
        devices = NTgCalls.get_media_devices().microphone
        return MediaDevices._parse_devices(devices, False)

    @staticmethod
    def speaker_devices() -> List:
        devices = NTgCalls.get_media_devices().speaker
        return List(
            SpeakerDevice(
                device.name,
                device.metadata,
            )
            for device in devices
        )

    @staticmethod
    def camera_devices() -> List:
        devices = NTgCalls.get_media_devices().camera
        return MediaDevices._parse_devices(devices, True)

    @staticmethod
    def screen_devices() -> List:
        devices = NTgCalls.get_media_devices().screen
        return List(
            ScreenDevice(
                device.name,
                device.metadata,
            )
            for device in devices
        )
