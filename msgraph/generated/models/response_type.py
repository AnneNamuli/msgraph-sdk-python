from enum import Enum

class ResponseType(Enum):
    None_ = "none",
    Organizer = "organizer",
    TentativelyAccepted = "tentativelyAccepted",
    Accepted = "accepted",
    Declined = "declined",
    NotResponded = "notResponded",

