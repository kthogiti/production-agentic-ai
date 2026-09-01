
from devteam.models.developer_profile import DeveloperProfile

def get_developer(
    developer_id: str,
) -> DeveloperProfile:

    for developer in DEVELOPERS:
        if developer.id == developer_id:
            return developer

    raise ValueError(
        f"Unknown developer: {developer_id}"
    )

DEVELOPERS = [
    DeveloperProfile(
        id="DEV-001",
        name="Developer 1",
        skills=[
            "C#",
            "ASP.NET Core",
            "React",
            "SQL",
            "Testing",
        ],
    ),
    DeveloperProfile(
        id="DEV-002",
        name="Developer 2",
        skills=[
            "C#",
            "ASP.NET Core",
            "React",
            "SQL",
            "Testing",
        ],
    ),
]