# Contributing to Bay FC 2026 Schedule Sync

First, thank you for wanting to make this calendar better for the Bay FC community! 

Since the `.ics` file is generated automatically, **please do not edit `schedule.ics` directly**. All changes should be made to `schedule.json`.

## How to Add Match Details
The `schedule.json` file is pre-populated with empty fields for additional matchday information. To contribute, simply find the match you have information for and fill in the blank quotes.

You can add:
* **`broadcast`**: Where to watch (e.g., "NWSL+", "Amazon Prime", "ION")
* **`theme`**: Theme nights (e.g., "Pride Night", "Fan Appreciation")
* **`giveaway`**: In-stadium giveaways (e.g., "Bobbleheads", "Rally Towels")
* **`halftime`**: Halftime shows or special events

**Example:**
If you know the home opener is on Amazon Prime and giving away towels, change this:
```json
{
  "date": "2026-03-21",
  "time": "17:45",
  "opponent": "Angel City FC",
  "is_home": true,
  "broadcast": "",
  "theme": "",
  "giveaway": "",
  "halftime": ""
}
```
to this:
```
{
  "date": "2026-03-21",
  "time": "17:45",
  "opponent": "Angel City FC",
  "is_home": true,
  "broadcast": "Amazon Prime",
  "theme": "Home Opener",
  "giveaway": "Rally Towels",
  "halftime": ""
}
```

## Submitting Your Changes
1. Fork the repository.
1. Update the fields in schedule.json.
1. Commit your changes and push them to your fork.
1. Open a Pull Request!

The generator script will automatically format your additions into the calendar descriptions the next time it runs. If you want to add a completely new data category that isn't listed above, please open an issue to discuss it, as that will require a small update to the Python script.

