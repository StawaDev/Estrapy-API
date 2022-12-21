# Changelog

A notice containing the modifications from this project will be included in each published version.
Please submit an **[issue](https://github.com/StawaDev/Estrapy-API/issues)** if you believe something is missing.

### 「0.2.8」 » Dec. 21, 2022

_If you're concerned by these changes, you may always look at examples._

#### Changed Features

- Changed return list into `PropertiesManager.url` when user use `generate` parameter.
- Updated `Base` class
- Updated CLI
- Updated requirements packages
- Formatted source codes
- Renamed `user_id` & `token_id` » `client_id` and `client_secret`
- Renamed `OsuClient` properties `client_id` & `client_secret` » `osu_client_id` & `osu_client_secret`

#### Added Features

- Added `original_response` to `PropertiesManager`
- Added `Requester` class
- Added `AccountProperties` class
- Added `AccountStatistics` class
- Added a `Test Requests` on CLI
- Added PATH file for Trivia

### 「0.2.7」 » Oct. 23, 2022

<details>
    <summary><span class="emoji">📃</span><b> View Previous Updates</b></summary>

<span class="emoji">🚧</span> _**If you are upgrading to v0.2.7, please see [Examples](https://github.com/StawaDev/Estrapy-API/tree/main/Examples)**._

#### Changed Features

- Fixed loop `save()` when saving files
- Formatted & Simplified Code of the `AutoUpdate` class
- Moved `trivia` & `osu` class from `games.py` to its own category file
- Updated host url (`base_url`)
- Updated description of this project
- Updated the `cli` functions

#### Added Features

- Added `post_api` to `http.py`
- Added `InvalidNumber` error
- Added Maintain Track of Requests
- Added `PropertiesManager` class
- Added `user_id` & `user_token` to every category class (`EstraClient`)

#### Removed Features

- Removed `@staticmethod` from every category class
- Removed `Data` class
- Removed `ObjectConverter` from `base`

</details>
