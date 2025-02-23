# TheRiffler

**Description**
The Riffler - an Arduino-based guitar-playing robot that uses servomotors to simultaneously press frets and pluck strings. Our system includes a custom Python parser that converts Guitar Pro (.gp5) files storing guitar tablatures, which are essentially sheet music, but for guitars, into a structured JSON file for each song, detailing which frets and strings to play for each note. This data is transmitted in real time via Arduino’s serial connection from the Python script to trigger our calibrated servo positions. Featuring a curated collection of 20 Canadian classics, The Riffler will perform guitar songs live to honor our country and unite us as a community, as a country, and as C

**Idea:** Guitar playing robot: With Arduino servomotors so it'll press on the frets and pluck the strings at the same time to play songs,
the songs will be Canadian classics since everyone in Canada these days are becoming less and less patriotic, especially with the recent
tariffs, we'll have to stand with each other as a community, as a country, as Canadians.

**What we'll need to do:**
* Find a dataset of 20 Canadian songs in guitar tabs/MIDI
* Make a Python script that'll automatically parse through the guitar songs' data
* Manually adjust the MIDI/tabs for the notes and timings to put it into Arduino
* Guitar will play random Canadian songs from the collection that we chose -> Useless/Unique Hack

* Step 1: Parse data from tablature to array of tuple (or similar) => (time to execute cmd, cmd (unpress/press), duration of cmd, string #, fret #)
* Step 2: Simulate song (time frame) and send info to arduino (print to terminal for now).

**Packages & Dependencies:**
* Create virtual environment by running `python3 -m venv guitar_env`
* Activate virtual environment by running `guitar_env\Scripts\activate`
* `pip install pyguitarpro`
* Run `python parse_guitar.py` to parse .gp5 file (make sure to change path to where you put it)
* Modify the parsed JSON file to the right fret numbers

**How to get the GuitarPro (.gp5) files:**
* Find desired tabs on songsterr.com
* Download .gp5 file from https://www.songsterr-downloader.com/
* Run script