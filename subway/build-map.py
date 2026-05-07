#!/usr/bin/env python3
"""Build the OpenAI API tube-style map.

22 APIs across 5 product lines — Conversational, Specialized AI,
Assistants, Models & Training, Real-time & Tools.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Chat Completions": "Chat Completions",
}

LINES = [
    {
        "name": "Conversational AI",
        "color": "#10A37F",  # OpenAI green
        # Concave-up arc.
        "stations": [
            ("Chat",             (260, 200)),
            ("Chat Completions", (440, 175)),
            ("Completions",      (620, 165)),
            ("Responses",        (810, 175)),
            ("Conversations",    (1000, 200)),
        ],
    },
    {
        "name": "Specialized AI",
        "color": "#E68B1F",
        # Sine wave.
        "stations": [
            ("Embeddings",  (270, 320)),
            ("Moderations", (430, 295)),
            ("Audio",       (590, 320)),
            ("Images",      (760, 295)),
            ("Videos",      (920, 320)),
        ],
    },
    {
        "name": "Assistants",
        "color": "#7B3FE4",
        # L-shape: vertical drop on the left then 45° bend right.
        "stations": [
            ("Assistants",    (260, 430)),
            ("Threads",       (260, 510)),
            ("Vector Stores", (310, 575)),
            ("Files",         (410, 615)),
        ],
    },
    {
        "name": "Models & Training",
        "color": "#1E5BD0",
        # Horizontal middle.
        "stations": [
            ("Models",      (510, 470)),
            ("Fine-tuning", (650, 460)),
            ("Evals",       (790, 470)),
            ("Batch",       (920, 460)),
        ],
    },
    {
        "name": "Real-time & Tools",
        "color": "#C5318B",
        # Closed-diamond loop at the bottom-right.
        "closed": True,
        "stations": [
            ("Realtime",   (820, 650)),
            ("ChatKit",    (910, 730)),
            ("Containers", (820, 810)),
            ("Uploads",    (730, 730)),
        ],
    },
]

# Override "Realtime API" to point to realtime-api (since "Realtime" alone
# would conflict with the canonical openai-realtime-api).
URL_OVERRIDES = {
    "Chat":             "https://apis.apis.io/apis/openai/openai-chat-api/",
    "Chat Completions": "https://apis.apis.io/apis/openai/openai-chat-completions-api/",
    "Completions":      "https://apis.apis.io/apis/openai/openai-completions-api/",
    "Responses":        "https://apis.apis.io/apis/openai/openai-responses-api/",
    "Conversations":    "https://apis.apis.io/apis/openai/openai-conversations-api/",
    "Embeddings":       "https://apis.apis.io/apis/openai/openai-embeddings-api/",
    "Moderations":      "https://apis.apis.io/apis/openai/openai-moderations-api/",
    "Audio":            "https://apis.apis.io/apis/openai/openai-audio-api/",
    "Images":           "https://apis.apis.io/apis/openai/openai-images-api/",
    "Videos":           "https://apis.apis.io/apis/openai/openai-videos-api/",
    "Assistants":       "https://apis.apis.io/apis/openai/openai-assistants-api/",
    "Threads":          "https://apis.apis.io/apis/openai/openai-threads-api/",
    "Vector Stores":    "https://apis.apis.io/apis/openai/openai-vector-stores-api/",
    "Files":            "https://apis.apis.io/apis/openai/openai-files-api/",
    "Models":           "https://apis.apis.io/apis/openai/openai-models-api/",
    "Fine-tuning":      "https://apis.apis.io/apis/openai/openai-fine-tuning-api/",
    "Evals":            "https://apis.apis.io/apis/openai/openai-evals-api/",
    "Batch":            "https://apis.apis.io/apis/openai/openai-batch-api/",
    "Realtime":         "https://apis.apis.io/apis/openai/openai-realtime-api/",
    "ChatKit":          "https://apis.apis.io/apis/openai/openai-chatkit-api/",
    "Containers":       "https://apis.apis.io/apis/openai/openai-containers-api/",
    "Uploads":          "https://apis.apis.io/apis/openai/openai-uploads-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The OpenAI API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: openai/openapi/*.yml · github.com/api-evangelist/openai",
        out_dir=Path(__file__).resolve().parent,
        out_basename="openai-subway-map",
        provider_id="openai",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
