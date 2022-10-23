# Changelog

A notice containing the modifications from this project will be included in each published version.
Please submit an **[issue](https://github.com/StawaDev/Estrapy-API/issues)** if you believe something is missing.

## [0.2.7] - 2022-10-24

<span class="emoji">🚧</span> _**If you are upgrading to v0.2.7, please see [Examples](https://github.com/StawaDev/Estrapy-API/tree/main/Examples)**._

### Changed Features

- Added `post_api` to `http.py`
- Added `InvalidNumber` error
- Fixed loop `save()` when saving files
- Formatted & Simplified Code of the `AutoUpdate` class
- Moved `trivia` & `osu` class from `games.py` to its own category file
- Updated host url (`base_url`)
- Updated description of this project
- Updated the `cli` functions

### Added Features

- Added Maintain Track of Requests
- Added `PropertiesManager` class
- Added `user_id` & `user_token` to every category class (`EstraClient`)

### Removed Features

- Removed `@staticmethod` from every category class
- Removed `ObjectConverter` from `base`
