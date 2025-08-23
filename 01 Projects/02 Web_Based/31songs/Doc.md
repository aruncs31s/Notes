---
tags: [31songs, backend, go, api, docs- Sessions & Last Played
	- Create lightweight sessions
	- Save a "last played" snapshot (trackId, position, isPlaying, volume, deviceId)
	- Auto-save last played when updating playback state if `X-Session-ID` is provided
	- **Restore playback** from last played snapshot (sets global playback state)
- Recently Played
	- Track listening history with timestamps
	- Get recent tracks (all or unique)
	- Top tracks with play counts
	- Statistics (total plays, completion rate)
	- Auto-tracked on playback state changes
	- Persisted to `data/recently_played.json`tle: 31Songs Go Backend – Features & API
---

# 31Songs Go Backend – Features & API

> Backend for the Local Player/31songs. REST + Socket.IO, sessions, last-played persistence. This page is Obsidian-friendly.

## [[Overview]]
- Language: Go
- Framework: Gin
- Realtime: Socket.IO-compatible endpoint
- Persistence:
	- Playlists → `data/playlists.json`
	- Sessions & Last Played → `data/sessions.json`
	- Recently Played → `data/recently_played.json`
	- Music library scanned from `MUSIC_DIR`

## [[Configuration]]
- Environment variables:
	- `HOST` (default: `0.0.0.0`)
	- `PORT` (default: `5000`)
	- `MUSIC_DIR` (default: `~/Music`)
- CORS is permissive for development; request headers allowed include `X-Device-ID` and `X-Session-ID`.

## [[Features]]
- Music Library
	- Scans audio files and extracts tags (title, artist, album, etc.)
	- Aggregates Albums and Artists
	- Search tracks, albums, artists
- Playlists
	- CRUD, add/remove/reorder tracks
	- Stats (track count and total duration)
	- Persisted to JSON
- Streaming
	- HTTP range requests supported for efficient seeking
	- Content types inferred by file extension
- Devices & Playback
	- Track connected devices
	- Set active device
	- Broadcast playback state and device list
	- Forward commands to active device
- Sessions & Last Played
	- Create lightweight sessions
	- Save a “last played” snapshot (trackId, position, isPlaying, volume, deviceId)
	- Auto-save last played when updating playback state if `X-Session-ID` is provided

## [[Models]]
- Track: `id`, `title`, `artist`, `album`, `duration`, `genre`, `year?`, `track?`, `filePath`, `fileName`, `hasAlbumArt`, `albumArtKey?`
- Album: `album`, `artist`, `trackCount`, `year?`, `tracks[]`, `hasAlbumArt`, `albumArtKey?`
- Artist: `name`, `trackCount`, `albums[]`
- Playlist: `id`, `name`, `description`, `tracks[]`, `createdAt`, `updatedAt`
- Device: `id`, `name`, `type`, `userAgent`, `ip`, `connectedAt`, `lastSeen`, `isActive`, `capabilities`
- PlaybackState: `currentTrack?`, `isPlaying`, `currentTime`, `volume`, `queue[]`
- PlaybackCommand: `command`, `data`
- Session: `id`, `createdAt`, `lastActive`, `lastPlayed?`
- LastPlayed: `trackId`, `position`, `isPlaying`, `volume`, `deviceId`, `updatedAt`
- RecentlyPlayedEntry: `trackId`, `playedAt`, `deviceId`, `sessionId`, `duration`, `completed`

## [[Services]]
- MusicLibraryService
	- Scan `MUSIC_DIR`, extract tags, build Artists/Albums
	- Search (tracks, albums, artists), library stats
- PlaylistService
	- Load/Save `data/playlists.json`
	- CRUD, add/remove/reorder tracks, stats
- StreamingService
	- Stream audio with HTTP ranges
	- MIME detection from extension
	- Album art extraction: TODO
- DeviceService
	- Devices map + active device
	- Global playback state
	- Broadcast device list + playback updates; forward commands
- SessionService
	- Load/Save `data/sessions.json`
	- Create, Touch, Get, SetLastPlayed, GetLastPlayed
- RecentlyPlayedService
	- Load/Save `data/recently_played.json`
	- Track listening history, get recent/unique/top tracks
	- Statistics and cleanup functionality

## [[HTTP API]]
Base path: `/api`

### System
- `GET /api/system/info`
- `POST /api/system/scan`

### Tracks
- `GET /api/tracks`
- `GET /api/tracks/:id`
- `GET /api/tracks/:id/stream`
- `GET /api/tracks/:id/album-art` (Not Implemented)
- `GET /api/tracks/search?q=`

### Albums
- `GET /api/albums`
- `GET /api/albums/:artist/:album`
- `GET /api/albums/search?q=`

### Artists
- `GET /api/artists`
- `GET /api/artists/:name`
- `GET /api/artists/search?q=`

### Playlists
- `GET /api/playlists`
- `POST /api/playlists`
- `GET /api/playlists/:id`
- `PUT /api/playlists/:id`
- `DELETE /api/playlists/:id`
- `GET /api/playlists/:id/tracks`
- `POST /api/playlists/:id/tracks`
- `DELETE /api/playlists/:id/tracks/:trackId`
- `PUT /api/playlists/:id/tracks/reorder`
- `GET /api/playlists/:id/stats`

### Devices
- `GET /api/devices`
- `GET /api/devices/active`
- `PUT /api/devices/active`
- `GET /api/devices/playback`
- `PUT /api/devices/playback`
- `POST /api/devices/playback/command`
- Headers: `X-Device-ID` optional (for command attribution)

### Sessions & Last Played
- `POST /api/sessions` → create a session
- `PUT /api/sessions/:id/touch` → update session last active
- `GET /api/sessions/:id/last-played` → get last played snapshot
- `PUT /api/sessions/:id/last-played` → set last played snapshot
- `POST /api/sessions/:id/restore` → **restore playback from last played snapshot**
- Auto-save on playback updates: include `X-Session-ID: <sessionId>` header on `PUT /api/devices/playback` to persist a snapshot.

### Recently Played
- `GET /api/recently-played` → get recently played tracks (with track details)
- `GET /api/recently-played/unique` → get recently played tracks without duplicates
- `GET /api/recently-played/stats` → get statistics about recently played tracks
- `GET /api/recently-played/top` → get most frequently played tracks
- `POST /api/recently-played/add` → manually add a track to recently played history
- `GET /api/recently-played/session/:sessionId` → get recently played tracks for a specific session

## [[WebSocket]]
- Endpoint: `GET /api/ws` (Socket.IO-compatible)
- Room: `devices`
- Inbound events:
	- `register_device` (DeviceInfo)
	- `playback_command` (PlaybackCommand)
	- `set_active_device` (deviceId)
	- `sync_playback_state` (state)
- Broadcast events:
	- `device_list`
	- `command`
	- `active_device_changed`
	- `playback_state_update`

## [[Run & Build]]
Run locally
```sh
HOST=127.0.0.1 PORT=5000 MUSIC_DIR=/path/to/music go run .
```

Build binary
```sh
go build -o bin/server .
```

## [[API Examples]]

### Health
```sh
curl -s http://localhost:5000/health
```

### System Info
```sh
curl -s http://localhost:5000/api/system/info | jq .
```

### Create Session
```sh
curl -s -X POST http://localhost:5000/api/sessions | jq .
```

### Touch Session
```sh
curl -s -X PUT http://localhost:5000/api/sessions/<sessionId>/touch | jq .
```

### Set Last Played
```sh
curl -s -X PUT http://localhost:5000/api/sessions/<sessionId>/last-played \
	-H 'Content-Type: application/json' \
	-d '{"trackId":"<trackId>","position":61.2,"isPlaying":true,"volume":0.5,"deviceId":"<deviceId>"}' | jq .
```

### Get Last Played
```sh
curl -s http://localhost:5000/api/sessions/<sessionId>/last-played | jq .
```

### **Restore from Last Played** ⭐
```sh
curl -s -X POST http://localhost:5000/api/sessions/<sessionId>/restore | jq .
```

### Recently Played Examples ⭐
```sh
# Get recent tracks
curl -s http://localhost:5000/api/recently-played?limit=10 | jq .

# Get unique recent tracks (no duplicates)
curl -s http://localhost:5000/api/recently-played/unique?limit=5 | jq .

# Get top played tracks
curl -s http://localhost:5000/api/recently-played/top?limit=5 | jq .

# Get recently played stats
curl -s http://localhost:5000/api/recently-played/stats | jq .

# Add track manually to recently played
curl -s -X POST http://localhost:5000/api/recently-played/add \
	-H 'Content-Type: application/json' \
	-d '{"trackId":"<trackId>","deviceId":"<deviceId>","sessionId":"<sessionId>","duration":180.5,"completed":true}' | jq .

# Get recently played for specific session
curl -s http://localhost:5000/api/recently-played/session/<sessionId> | jq .
```

### Auto-save Last Played on Playback Update
```sh
curl -s -X PUT http://localhost:5000/api/devices/playback \
	-H 'Content-Type: application/json' \
	-H 'X-Session-ID: <sessionId>' \
	-d '{"isPlaying":true,"currentTime":42,"volume":0.7,"currentTrack":{"id":"<trackId>"}}' | jq .
```

### Stream Track
```sh
curl -I http://localhost:5000/api/tracks/<trackId>/stream
```

### Playlist CRUD
```sh
# Create
curl -s -X POST http://localhost:5000/api/playlists \
	-H 'Content-Type: application/json' \
	-d '{"name":"Faves","description":"Best"}' | jq .

# Add track
curl -s -X POST http://localhost:5000/api/playlists/<playlistId>/tracks \
	-H 'Content-Type: application/json' \
	-d '{"trackId":"<trackId>"}' | jq .

# Reorder tracks
curl -s -X PUT http://localhost:5000/api/playlists/<playlistId>/tracks/reorder \
	-H 'Content-Type: application/json' \
	-d '{"trackIds":["<trackId1>","<trackId2>"]}' | jq .
```

## [[Testing Log]]
- Build: PASS (`go build ./...`)
- Server run: PASS (listening on configured host/port)
- System Info: PASS (200)
- Sessions:
	- Create: PASS (returns id)
	- Set/Get Last Played: PASS
	- **Restore Last Played: PASS** (restores track, position, volume, updates global state)
	- Auto-save via `PUT /api/devices/playback` + `X-Session-ID`: PASS
- Recently Played:
	- **Get Recent: PASS** (returns tracks with full details)
	- **Stats: PASS** (total entries, unique tracks, completion rate)
	- **Top Tracks: PASS** (play counts and timestamps)
	- **Manual Add: PASS** (manual entry addition)
	- **Auto-tracking: PASS** (tracks on playback updates)

## [[Notes & Next Steps]]
- WebSocket: optionally persist LastPlayed when receiving `sync_playback_state` (add optional `sessionId` param)
- Call `PlaylistService.LoadPlaylists()` on startup to preload existing playlists
- Implement album art extraction and caching in `StreamingService.GetAlbumArt`

## [[Recently Played Feature Details]]
The recently played system:
1. **Auto-tracks** when playback state changes with `X-Session-ID` header
2. **Stores entries** with: trackId, playedAt, deviceId, sessionId, duration, completed
3. **Provides analytics**: stats, top tracks, play counts
4. **Enriches responses** with full track details (title, artist, album, etc.)
5. **Persists to disk** in `data/recently_played.json` 
6. **Configurable limits** (max 100 entries by default)
7. **Session filtering** to get history per session/device

This enables "what did I listen to" and "most played tracks" functionality across sessions.


## Tests

```bash
TS2307: Cannot find module './components/StatsView' or its corresponding type declarations.
     5 | import { useLastPlayed } from './hooks/useLastPlayed';
     6 | import { useListeningTracker } from './hooks/useListeningTracker';
  >  7 | import StatsView from './components/StatsView';
       |                       ^^^^^^^^^^^^^^^^^^^^^^^^
     8 | import StatsWidget from './components/StatsWidget';
     9 |
    10 | interface Track {
```

```bash
echo "=== Testing Sessions ===" && SESSION_ID=$(curl -s -X POST http://127.0.0.1:5000/api/sessions | jq -r '.data.id') && echo "Created session: $SESSION_ID" && curl -s -X PUT http://127.0.0.1:5000/api/sessions/$SESSION_ID/touch | jq -c '.data.message'
```
```
=== Testing Sessions ===
Created session: a6f42cb7-9d58-48a4-b876-cd6168a8da44
"session touched"
```
```bash
echo "=== Testing Tracks ===" && TRACK_ID=$(curl -s http://127.0.0.1:5000/api/tracks | jq -r '.[0].id') && echo "Got track ID: $TRACK_ID" && curl -s http://127.0.0.1:5000/api/tracks/$TRACK_ID | jq -c '{id: .id, title: .title, artist: .artist}'
```
```
=== Testing Tracks ===
Got track ID: f588aa3f-f759-4d23-a753-8df7e56d9a56
{"id":"f588aa3f-f759-4d23-a753-8df7e56d9a56","title":"Die With A Smile","artist":"Lady Gaga, Bruno Mars"}
```


```bash
echo "=== Testing Last Played ===" && SESSION_ID="a6f42cb7-9d58-48a4-b876-cd6168a8da44" && TRACK_ID="f588aa3f-f759-4d23-a753-8df7e56d9a56" && curl -s -X PUT http://127.0.0.1:5000/api/sessions/$SESSION_ID/last-played -H 'Content-Type: application/json' -d "{\"trackId\":\"$TRACK_ID\",\"position\":45.2,\"isPlaying\":true,\"volume\":0.8,\"deviceId\":\"test-device\"}" | jq -c '.data.message' && echo "Getting last played:" && curl -s http://127.0.0.1:5000/api/sessions/$SESSION_ID/last-played | jq -c '.data | {trackId, position, isPlaying}'
```

```
=== Testing Last Played ===
"last played updated"
Getting last played:
{"trackId":"f588aa3f-f759-4d23-a753-8df7e56d9a56","position":45.2,"isPlaying":true}
```

```bash
❯ echo "=== Testing Restore Last Played (Raw) ===" && SESSION_ID="a6f42cb7-9d58-48a4-b876-cd6168a8da44" && curl -s http://127.0.0.1:5000/api/sessions/$SESSION_ID/restore-last-played
                                                                                                             

```
```
=== Testing Restore Last Played (Raw) ===
404 page not found      
```

```bash

echo "=== Testing Recently Played - Manual Add ===" && SESSION_ID="a6f42cb7-9d58-48a4-b876-cd6168a8da44" && TRACK_ID="f588aa3f-f759-4d23-a753-8df7e56d9a56" && curl -s -X POST http://127.0.0.1:5000/api/recently-played -H 'Content-Type: application/json' -d "{\"trackId\":\"$TRACK_ID\",\"sessionId\":\"$SESSION_ID\",\"deviceId\":\"test-device\",\"duration\":180.5,\"completed\":true}"
````

```bash
echo "=== Testing Recently Played - Get Recent ===" && curl -s "http://127.0.0.1:5000/api/recently-played?limit=3" | jq -c '.data | {total: length, tracks: [.[] | {title: .track.title, artist: .track.artist, playedAt: .playedAt, completed}]}'
```


```json
{"total":3,"tracks":[{"title":"Blood (From \"Marco\")","artist":"Ravi Basrur, Dabzee, Rohith Siddappa, Vinayak Sasikumar","playedAt":null,"completed":null},{"title":"Blood (From \"Marco\")","artist":"Ravi Basrur, Dabzee, Rohith Siddappa, Vinayak Sasikumar","playedAt":null,"completed":null},{"title":"Sparkle - movie ver.","artist":"Radwimps","playedAt":null,"completed":null}]}
```


```bash
echo "=== Testing Restore Last Played ===" && SESSION_ID="a6f42cb7-9d58-48a4-b876-cd6168a8da44" && curl -s "http://127.0.0.1:5000/api/sessions/$SESSION_ID/restore-last-played" | jq -c '.data | {track: .track.title, position, isPlaying, volume}'
```


```bash
curl -s -X POST http://127.0.0.1:5000/api/sessions
```

```bash
SESSION_ID="15946c4b-7108-4b72-8238-d899abe0c723" && TRACK_ID="67c1b262-f254-41de-910c-bebd7f674bb8" && curl -s -X PUT http://127.0.0.1:5000/api/sessions/$SESSION_ID/last-played -H 'Content-Type: application/json' -d "{\"trackId\":\"$TRACK_ID\",\"position\":75.3,\"isPlaying\":false,\"volume\":0.9,\"deviceId\":\"test-device\"}" && echo -e "\n--- Now Restoring ---" && curl -s "http://127.0.0.1:5000/api/sessions/$SESSION_ID/restore-last-played" | jq -c '.data | {track: .track.title, position, isPlaying, volume}'
```


> [!abstract] 
> ```bash
> echo "=== Testing Restore Raw Response ===" && SESSION_ID="15946c4b-7108-4b72-8238-d899abe0c723" && curl -s "http://127.0.0.1:5000/api/sessions/$SESSION_ID/restore-last-played"
> ```


```json
{"data":{"fromSnapshot":{"trackId":"67c1b262-f254-41de-910c-bebd7f674bb8","position":75.3,"isPlaying":false,"volume":0.9,"deviceId":"test-device","updatedAt":"2025-08-24T00:45:15.380000068+05:30"},"message":"playback restored from last played","restoredState":{"currentTrack":{"id":"67c1b262-f254-41de-910c-bebd7f674bb8","title":"Kadhal Aasai","artist":"Yuvanshankar Raja, Sooraj Santhosh","album":"Anjaan (Original Motion Picture Soundtrack)","duration":0,"genre":"Indian Music \u0026 Films/Games \u0026 Film Scores","year":2014,"track":4,"filePath":"/home/aruncs/Music/TakeMeHome/Anjaan (Original Motion Picture Soundtrack) CD 1 TRACK 4 (32.mp3","fileName":"Anjaan (Original Motion Picture Soundtrack) CD 1 TRACK 4 (32.mp3","hasAlbumArt":true,"albumArtKey":"Yuvanshankar Raja, Sooraj Santhosh-Anjaan (Original Motion Picture Soundtrack)"},"isPlaying":false,"currentTime":75.3,"volume":0.9,"queue":[{"id":"67c1b262-f254-41de-910c-bebd7f674bb8","title":"Kadhal Aasai","artist":"Yuvanshankar Raja, Sooraj Santhosh","album":"Anjaan (Original Motion Picture Soundtrack)","duration":0,"genre":"Indian Music \u0026 Films/Games \u0026 Film Scores","year":2014,"track":4,"filePath":"/home/aruncs/Music/TakeMeHome/Anjaan (Original Motion Picture Soundtrack) CD 1 TRACK 4 (32.mp3","fileName":"Anjaan (Original Motion Picture Soundtrack) CD 1 TRACK 4 (32.mp3","hasAlbumArt":true,"albumArtKey":"Yuvanshankar Raja, Sooraj Santhosh-Anjaan (Original Motion Picture Soundtrack)"}]}},"error":false}
```