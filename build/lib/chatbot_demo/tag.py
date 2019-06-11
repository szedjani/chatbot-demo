from attr import dataclass


@dataclass
class Tag:
    id: int
    tag_category: str
    tag: str


TAGS = {
    "en": Tag(1, "Lang", "English"),
    "de": Tag(2, "Lang", "German"),
    "ltd": Tag(3, "Company Structure", "Ltd."),
    "plc": Tag(4, "Company Structure", "plc"),
    "shareholder": Tag(5, "", "Shareholder")
}
