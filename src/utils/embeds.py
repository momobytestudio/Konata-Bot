import discord


def create_embed(
    title: str | None = None,
    description: str | None = None,
) -> discord.Embed:
    """Create a standard Konata embed."""
    return discord.Embed(
        title=title,
        description=description,
    )


def success_embed(
    title: str = "Success",
    description: str | None = None,
) -> discord.Embed:
    """Create a standard success embed."""
    return discord.Embed(
        title=title,
        description=description,
    )


def error_embed(
    title: str = "Error",
    description: str | None = None,
) -> discord.Embed:
    """Create a standard error embed."""
    return discord.Embed(
        title=title,
        description=description,
    )


def info_embed(
    title: str = "Information",
    description: str | None = None,
) -> discord.Embed:
    """Create a standard information embed."""
    return discord.Embed(
        title=title,
        description=description,
    )