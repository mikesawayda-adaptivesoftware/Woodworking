# Entertainment Center

A white, four-module floating media cabinet with a joined painted-white top and a separate floor-supported subwoofer surround.

## Run the build companion

From this repository root:

```sh
python3 -m http.server 8000 --directory EntertainmentCenter
```

Open `http://localhost:8000/app/` in your browser. No packages, build step, external fonts, API keys, or network access are needed. Stop the server with Ctrl+C. You can also open `app/index.html` directly; browser storage behavior may vary for file URLs.

The app includes a selectable front elevation and plan view, sheet breakdowns, a thickness calculator, and a step-by-step checklist with PDF page references. Checkmarks and notes are stored only in the current browser, not synced to Git or other devices. Export a JSON backup and import it on another device to transfer progress. Printing includes all steps.

## Buy list

The website’s [buy list](app/index.html#buy-list) covers wood, connectors, lighting/power/cooling, finishes and tools. Quantities are allowances where supported by the guide; top/door/false-back stock and structural fasteners are marked for selection or measurement. Doors on the three equipment bays can be added later to the same four-box build. Purchase checkmarks persist separately in the browser; they are not included in build-progress export/import. Printing the build checklist also prints the buy list. Edit `app/shopping.js` to maintain the categorized items.

## Current design — Rev F

The current reference shows four closed white inset Shaker-style doors and an open 19″ subwoofer alcove, with one 112″ joined, filled and painted-white top. The four box widths remain 26″, 26″, 20″ and 21″; box panel dimensions are unchanged. Top depth is approximately 20¼″, field-fit. Top material and thickness, four-door construction/hardware, and ventilation details remain to be finalized. Finished height is 24½″ plus the selected top thickness. Reserve extra stock for the top and three additional doors; the original three-sheet layout is not the complete revised shopping list.

- [Current Rev F PDF](docs/entertainment-center-build-guide-rev-f.pdf): revised shopping, top, door and height notes plus the latest image on page 13 and top/ventilation details on page 14.
- [Current white-top image](assets/design-white-top.png).
- [White top with all doors removed](assets/design-white-top-open.png): website overview and enlarged cabinet-front view. Equipment and hidden construction are illustrative; this does not change the panel cut list.
- [Four-section open-bay comparison](assets/design-four-bays-open.png): the earlier wood-top option with three open equipment bays and only the far-right storage door. Displayed on the website for comparison; it does not replace the Rev F design.
- Rebuild Rev F with `python3 EntertainmentCenter/tools/build_current_pdf.py` (optional generation dependencies: PyMuPDF and reportlab).

## Historical source documents

- [Rev E with design reference](docs/entertainment-center-build-guide-rev-e-with-reference.pdf): the original twelve pages plus the supplied image on page 13. Existing page references remain unchanged.
- [Design reference image](assets/design-reference.png): the exact PNG supplied in the uploaded ZIP, retained with the historical PDF. It illustrates finishes and lighting; its bay and door arrangement does not supersede the dimensioned plan.

- [Original Rev E PDF](docs/entertainment-center-build-guide-rev-e.pdf), preserved unchanged from the supplied file.
- [Extracted text](docs/build-guide-rev-e.txt), searchable text extracted with `pdftotext -layout`.

The app follows Rev F; diagrams are dimensioned schematics, not fabrication templates. It does not calculate structural capacity. Permanent mounting-strip joinery, wall fasteners, blocking connections, the Denon outlet adaptation, and final top-joint/fastening details remain to be specified for the actual installation. Door hardware part numbers changed in the earlier conversation and are intentionally not presented as a verified purchase list.

## Project layout

`assets/` contains project reference images. `docs/` contains source plans. `app/` contains the dependency-free companion. Project data and construction steps live in `app/app.js`; styling lives in `app/style.css`.

## Checks

```sh
node --check EntertainmentCenter/app/app.js
```

Browser validation should cover selecting every bay, switching views, changing plywood thickness, checklist persistence, notes, progress backup/restore, PDF links, and the mobile layout.

## Regenerate the PDF appendix

The updated PDF is already checked in. To rebuild it, run `python3 EntertainmentCenter/tools/build_reference_pdf.py` from the repository root with `reportlab` and `pypdf` installed. These optional generation packages are not required to run the website. The script preserves the original PDF and appends one reference page.

## Docker / Unraid

The GitHub Actions workflow [entertainment-center-docker.yml](../.github/workflows/entertainment-center-docker.yml) follows the GHCR publishing pattern in Clippy's `main` branch. It builds and smoke-tests the container before publishing using GitHub's built-in `GITHUB_TOKEN`; no additional Actions secret is needed.

Image: `ghcr.io/mikesawayda-adaptivesoftware/woodworking-entertainment-center`

- Pushes to `work` publish `:work`; pushes to `main` publish `:main` and `:latest`.
- Each published build also gets a `:sha-<full commit>` tag.
- Pull requests build and test without publishing. The workflow can also run manually; weekly rebuilds run from GitHub's default branch. GitHub only registers scheduled/manual workflows on the default branch, so merge the workflow there to enable those triggers.
- The supplied template uses `:work` so it can be installed before these changes reach `main`. Switch to `:latest` after merging and the first successful main build.

### Install on Unraid

1. Wait for **Actions → Entertainment Center Docker image** to finish successfully for your selected branch.
2. In GitHub, open **Packages → woodworking-entertainment-center → Package settings**. If it is private, change visibility to public to allow anonymous pulls, or authenticate Unraid to GHCR with credentials that can read that package. Publishing alone does not make a new package public.
3. Copy [deploy/unraid/entertainment-center.xml](deploy/unraid/entertainment-center.xml) to `/boot/config/plugins/dockerMan/templates-user/my-entertainment-center.xml` on Unraid.
4. Open **Docker → Add Container**, select **entertainment-center**, and apply. Use bridge networking, leave privileged mode off, and map host port **8088** to container port **8080** (change 8088 if occupied).
5. Open `http://YOUR-UNRAID-IP:8088/app/`. The server root also redirects to the app.

No API keys or volume mappings are required. Plans and images are built into the container; checklist progress stays in each browser. Export progress before changing the hostname, protocol or port, since those changes use a separate browser storage location. Unraid's update check can pull newer images for the selected tag. No automatic updater is installed by this project.

### Other Docker hosts

```sh
docker compose -f EntertainmentCenter/deploy/compose.yml up -d
```

Or build and run locally from the repository root:

```sh
docker build -t entertainment-center:local EntertainmentCenter
docker run -d --name entertainment-center -p 8088:8080 --restart unless-stopped entertainment-center:local
```

The image serves static files with unprivileged Nginx on port 8080 and includes a `/healthz` endpoint. The app has no server-side accounts or progress database. The optional Python PDF-generation tools are not installed in the runtime image.
