from enum import Enum

class IosUpdatesInstallStatus(Enum):
    DeviceOsHigherThanDesiredOsVersion = "deviceOsHigherThanDesiredOsVersion",
    SharedDeviceUserLoggedInError = "sharedDeviceUserLoggedInError",
    NotSupportedOperation = "notSupportedOperation",
    InstallFailed = "installFailed",
    InstallPhoneCallInProgress = "installPhoneCallInProgress",
    InstallInsufficientPower = "installInsufficientPower",
    InstallInsufficientSpace = "installInsufficientSpace",
    Installing = "installing",
    DownloadInsufficientNetwork = "downloadInsufficientNetwork",
    DownloadInsufficientPower = "downloadInsufficientPower",
    DownloadInsufficientSpace = "downloadInsufficientSpace",
    DownloadRequiresComputer = "downloadRequiresComputer",
    DownloadFailed = "downloadFailed",
    Downloading = "downloading",
    Success = "success",
    Available = "available",
    Idle = "idle",
    Unknown = "unknown",

