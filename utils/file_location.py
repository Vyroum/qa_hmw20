from pathlib import Path


def path_to_file(relative_path: str):
    import resources
    return (Path(resources.__file__).parent.parent.joinpath(relative_path).absolute().__str__())
