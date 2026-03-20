import json
import uuid
from datetime import datetime, timedelta, timezone

# Gemini updated this Python script to dynamically build the description from optional JSON fields 
# using friendlier terms for the calendar event details.

def generate_ics(json_filepath, output_filepath):
    with open(json_filepath, 'r') as f:
        games = json.load(f)

    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Unofficial Bay FC Schedule//EN",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:Bay FC 2026 Schedule",
        "X-WR-TIMEZONE:America/Los_Angeles"
    ]

    for game in games:
        dt_str = f"{game['date']} {game['time']}"
        dt_start = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        dt_end = dt_start + timedelta(hours=2) 
        
        start_str = dt_start.strftime("%Y%m%dT%H%M%00")
        end_str = dt_end.strftime("%Y%m%dT%H%M%00")
        
        location = "PayPal Park, San Jose, CA" if game["is_home"] else "Away"
        summary = f"Bay FC vs {game['opponent']}" if game["is_home"] else f"Bay FC @ {game['opponent']}"
        
        # Dynamically build the event block
        event = [
            "BEGIN:VEVENT",
            f"UID:{uuid.uuid4()}@bayfcschedule",
            f"DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
            f"DTSTART;TZID=America/Los_Angeles:{start_str}",
            f"DTEND;TZID=America/Los_Angeles:{end_str}",
            f"SUMMARY:{summary}",
            f"LOCATION:{location}"
        ]

        # Check for optional details and build the description using friendly terms
        desc_elements = []
        if game.get("broadcast"):
            desc_elements.append(f"📺 Watch Live: {game['broadcast']}")
        if game.get("theme"):
            desc_elements.append(f"✨ Theme Night: {game['theme']}")
        if game.get("giveaway"):
            desc_elements.append(f"🎁 Stadium Giveaway: {game['giveaway']}")
        if game.get("halftime"):
            desc_elements.append(f"🎤 Halftime Show: {game['halftime']}")

        if desc_elements:
            # iCal requires literal '\n' characters for line breaks within a field
            description_string = "\\n".join(desc_elements)
            event.append(f"DESCRIPTION:{description_string}")

        event.append("END:VEVENT")
        ics_content.extend(event)

    ics_content.append("END:VCALENDAR")
    
    with open(output_filepath, "w") as f:
        f.write("\n".join(ics_content))
    
    print(f"Successfully generated {output_filepath}")

if __name__ == "__main__":
    generate_ics("schedule.json", "schedule.ics")
