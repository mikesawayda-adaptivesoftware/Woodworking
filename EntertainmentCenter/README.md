# Entertainment Center

A white, four-module floating media cabinet with a continuous wood cap and a separate floor-supported subwoofer surround.

## Run the build companion

From this repository root:

```sh
python3 -m http.server 8000 --directory EntertainmentCenter
```

Open `http://localhost:8000/app/` in your browser. No packages, build step, external fonts, API keys, or network access are needed. Stop the server with Ctrl+C. You can also open `app/index.html` directly; browser storage behavior may vary for file URLs.

The app includes a selectable front elevation and plan view, sheet breakdowns, a thickness calculator, and a step-by-step checklist with PDF page references. Checkmarks and notes are stored only in the current browser, not synced to Git or other devices. Export a JSON backup and import it on another device to transfer progress. Printing includes all steps.

## Source documents

- [Original Rev E PDF](docs/entertainment-center-build-guide-rev-e.pdf), preserved unchanged from the supplied file.
- [Extracted text](docs/build-guide-rev-e.txt), searchable text extracted with `pdftotext -layout`.

The app summarizes Rev E; diagrams are dimensioned schematics, not fabrication templates. It does not calculate structural capacity. Permanent mounting-strip joinery, wall fasteners, blocking connections, the Denon outlet adaptation, and slab movement details remain to be specified for the actual installation. Door hardware part numbers changed in the earlier conversation and are intentionally not presented as a verified purchase list.

## Project layout

`docs/` contains source plans. `app/` contains the dependency-free companion. Project data and construction steps live in `app/app.js`; styling lives in `app/style.css`.

## Checks

```sh
node --check EntertainmentCenter/app/app.js
```

Browser validation should cover selecting every bay, switching views, changing plywood thickness, checklist persistence, notes, progress backup/restore, PDF links, and the mobile layout.
