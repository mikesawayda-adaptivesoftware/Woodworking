'use strict';
// Quantities are planning allowances, not a finalized structural fastener schedule.
const shoppingGroups = [
 ['Wood and sheet goods', [
  ['cabinet-plywood','Cabinet-grade veneer-core plywood','3 sheets · 4 × 8′ · nominal ¾″','Base build','Original box, shelf and surround layout, plus one rough door blank. Measure actual thickness. Extra top, false-back and optional-door material is separate.'],
  ['white-top','Joined painted-white top stock','112″ × approximately 20¼″ finished','Select first','Choose substrate, thickness and seam joinery before buying. Make a cutting layout to determine sheets; do not buy the old butcher-block blank. Retain all plywood box tops.'],
  ['top-joint','Top seam backing / alignment stock','To suit selected joint','Select first','Locate seam over support, away from a box joint. Choose substrate-appropriate backing/joinery and compatible fasteners; filler is cosmetic.'],
  ['face-trim','Paint-grade poplar face trim','Two 8′ rails + stock for 5 vertical strips','Base build','¼″-thick trim. Each long rail fits the 93″ run; 3 seam covers and 2 end strips fit between rails. Match widths to actual plywood edges.'],
  ['mount-strips','Straight, dry mounting-strip stock','Two 8′ nominal 2×4s · provisional','Verify mounting','Rev F allowance for 8 rear strips: four about 24½″, two about 18½″, two about 19½″ with true ¾″ sides. Fit to actual openings; adapt Denon outlets. Stock and joint design require verification.'],
  ['structural-cleats','Solid-wood mounting-strip cleats','Quantity and section TBD','Verify mounting','Separate from false-back cleats. Size their connections to sides and top/bottom for the hanging load.'],
  ['blocking','In-wall structural blocking + patch material','Measure actual stud bays','Verify mounting','Buy blocking stock and its connectors after mapping upper/lower anchors, wiring and outlets. Include matching drywall, backing, tape and joint compound where opened.'],
  ['ledger','Temporary installation ledger','One straight 8′ 2×4; cut to 93″','Base build','Separate from the permanent strips. Also provide a stable front platform or cabinet lift and a helper.'],
  ['false-backs','Paint-grade removable false-back panels','¼″ plywood · field-fit each bay','Measure first','Optional cable-concealment addition. Choose offset using actual plugs and cable bends; test receiver depth before buying/cutting. Split panels where needed for access. Not included in the original 3-sheet allowance.'],
  ['back-cleats','Small solid-wood false-back cleats','Field-fit supports per removable panel','Measure first','Nonstructural supports fixed to cabinet sides. Determine cross-section, offset and screw paths before cutting; keep clear of wall mounts and equipment.'],
  ['doors','Inset door materials','1 storage door; up to 3 more optional','Select first','Same four boxes with any door count. Select flat-panel or Shaker construction, thickness and reveals first. The original single plywood blank is not a complete Shaker-door material list.'],
 ]],
 ['Fasteners and connectors', [
  ['pockets','Coarse-thread pocket-hole screws','Box-joint count + test pieces','Base build','1¼″ is the guide’s starting size for true ¾″ plywood. Match jig and screw to measured stock and test on offcuts.'],
  ['wood-screws','Wood screws for strips and cleats','Per verified joint layout','Select first','Choose length, head, pilot holes and spacing for each joint. Keep tips inside intended material; pocket screws alone do not establish hanging capacity.'],
  ['wall-fasteners','Rated cabinet / structural wall fasteners','Per verified anchorage schedule','Verify mounting','Select after confirming strip thickness, drywall, framing, required embedment and loaded weight. Include specified washers. Do not substitute drywall screws.'],
  ['block-connectors','Blocking attachment screws / connectors','Per verified blocking detail','Verify mounting','Secure blocking to studs with suitable connections before patching; document locations.'],
  ['cabinet-connectors','Cabinet connector screws / bolts','For 3 paired-side joints','Select first','Size for the combined side thickness; keep tips within paired panels. These align boxes and do not replace each box’s wall attachments.'],
  ['back-fasteners','Removable-back screws or panel clips','To suit each panel support layout','Measure first','Use front-accessible, removable fasteners. Keep outlet covers and plugs serviceable; do not glue false backs in place.'],
  ['shelf-pins','Shelf pins and matching drill bit','4 supports per shelf, typically','Optional','For storage and optional Switch shelf. Confirm pin diameter and shelf clearance, especially around hinges.'],
  ['door-hinges','Inset hinges + matching mounting plates','Typically 2 hinges + 2 plates per door; verify load','Optional doors','One hinge plus one plate at each hinge position (typically 2 hinges and 2 plates per door). Final count depends on door size/weight; verify the manufacturer’s chart.'],
  ['door-opening','Door pulls/stops OR push-to-open latches','One opening system per door','Select first','Self-closing/soft-close hinges with a pull and an inset stop, OR compatible free-swing hinges with inset-rated push latch/catch/adapter. Do not mix systems without confirmed compatibility.'],
  ['grommets','Cable grommets / edge protection','Count cable passages after layout','Measure first','Size holes for the largest connector, not just the cable. Plan inter-bay routes before assembly, clear of hinges and structural strips.'],
  ['shims','Stable cabinet shims and leveling pads','Assorted pack','Base build','Shim at anchorage points; provide firm, stable bearing under the subwoofer surround on carpet.'],
 ]],
 ['Lighting, power and cooling', [
  ['led-tape','Warm-white dimmable LED tape','7¾′ underside + optional interior lengths','Select first','24 V COB, 2700–3000 K is the suggested starting point. Match strip width, wattage, controller and driver. Interior lighting is optional behind opaque doors.'],
  ['led-channels','Recessed aluminum LED channels + diffusers','93″ underside + selected interior runs','Select first','Buy the actual shallow, flanged profile before choosing a router bit or groove depth. Verify remaining plywood thickness and mounting method. Include end caps and retention hardware.'],
  ['led-power','LED power supply / driver','Sized from total strip wattage','Select first','Follow maker’s sizing margin and maximum run limits. Keep driver accessible, ventilated and clear of receiver heat.'],
  ['led-control','Compatible dimmers / controllers','Up to 2 independently controlled zones','Optional','Separate underside and interior zones if both are installed; confirm voltage, current and dimming compatibility.'],
  ['led-wire','Low-voltage wire and connectors','Measure routes; allow service slack','Select first','Match current and voltage-drop requirements. Include tape-to-wire connectors or solder/heat-shrink supplies, strain relief and accessible disconnects across box seams.'],
  ['power-strip','Listed power strip / surge protector','Sized for equipment and accessible location','Select first','Check plug orientation and cord reach. Keep its switch and plugs reachable; ordinary power cords must not run inside wall cavities.'],
  ['cooling','Vents, fans and temperature controller','After airflow layout and heat-load check','If enclosing equipment','Provide room-air intake and exhaust back to the room. Inter-bay holes only connect that path. Select fans/grilles, power supply and controller together; test with doors closed.'],
  ['cable-ties','Cable clips / reusable hook-and-loop ties','One assorted pack','Useful','Secure cables with service slack; avoid hot vents, sharp edges, hinge travel and tight bends.'],
 ]],
 ['Glue, finish and consumables', [
  ['glue','Wood adhesive compatible with substrate','Enough for boxes, trim and selected top joint','Base build','Glue bare mating surfaces and follow clamp/cure instructions. Do not rely on filler to connect the top.'],
  ['filler','Paint-grade filler / edge sealer','Small test quantity, then project quantity','Select first','Use a compatible filler over a stable seam and plywood edges. MDF and plywood need different edge preparation.'],
  ['paint','Primer and white cabinet/top paint','Coverage from selected coating system','Select first','Choose a durable compatible finish, account for coats and all painted surfaces, and make a seam/finish sample. Allow full cure.'],
  ['abrasives','Sandpaper, sanding block and dust removal supplies','Assorted grits to coating instructions','Base build','Include brush/roller supplies, masking tape, drop cloths and clean rags.'],
  ['patch','Drywall primer and matching wall paint','As required by blocking / ledger holes','If opening wall','Joint compound and tape are listed with wall-blocking stock.'],
 ]],
 ['Tools to own, borrow or rent', [
  ['measure-tools','Tape, pencil, square, straightedge and caliper','One measuring kit','Needed','Caliper for actual plywood thickness; square and tape for diagonals.'],
  ['cut-tools','Track saw or circular saw with guide; suitable blade','One accurate cutting setup','Needed','Support full sheets safely with a cutting table or sacrificial support. A table saw is another option, not an additional requirement.'],
  ['drill-tools','Drill/driver, bits, countersink and pocket-hole jig','One set plus correct driver bits','Needed','Use a low clutch setting and practice on offcuts. Add connector-size hole saws after choosing grommets.'],
  ['clamp-tools','Assembly clamps and flat work surface','Enough to hold each box square','Needed','Have suitable clamps for face alignment and the top joint; test the clamping layout before applying glue.'],
  ['wall-tools','Long level or laser, stud finder, drywall tools','To suit wall work','Needed','Verify stud centers and check for wiring. Use appropriate circuit testing before opening near outlets.'],
  ['router-tools','Router, straightedge/jig and profile-matched bit','For chosen recessed LED channels','If recessing lights','Select the channel first. Test groove width/depth in actual plywood; keep away from pocket screws, mounting joints and door hardware.'],
  ['hinge-tools','Hinge drilling jig and cup bit (often 35 mm)','To chosen hinge specifications','If adding doors','Confirm cup diameter, depth and setback before drilling; test the complete hinge/trim geometry on scrap.'],
  ['shelf-jig','Shelf-pin drilling jig','Matched to chosen pins','Optional','For adjustable shelving; drill while panels are accessible.'],
  ['sanding-tools','Sander and/or sanding blocks; dust extraction','One finishing setup','Needed','Useful for the top seam and white finish; use substrate/coating-appropriate abrasives.'],
  ['install-tools','Stable front support or cabinet lift','One installation setup + helper','Needed','The rear ledger alone does not support the front of the 20″-deep boxes while mounting.'],
  ['ppe','Eye/hearing protection and suitable dust protection','For every person doing the work','Needed','Use dust extraction and protection appropriate to cutting, sanding and coating products.'],
 ]],
];
const buyKey='woodworking.entertainment-center.shopping.v1';
let purchased=[];
const allIds=new Set(shoppingGroups.flatMap(([,items])=>items.map(([id])=>id)));
const buyStatus=document.getElementById('buy-status');
try {const saved=JSON.parse(localStorage.getItem(buyKey));if(Array.isArray(saved))purchased=[...new Set(saved.filter(id=>allIds.has(id)))];}catch{buyStatus.textContent='Browser storage is unavailable; print a copy to keep your list.';}
const buyGroups=document.getElementById('buy-groups');
for(const [name,items] of shoppingGroups){
 const group=document.createElement('details');group.open=true;
 const summary=document.createElement('summary');summary.textContent=`${name} · ${items.length} items`;group.append(summary);
 const list=document.createElement('ul');list.className='buy-items';
 for(const [id,name,quantity,stage,note] of items){
  const li=document.createElement('li');const label=document.createElement('label');label.className='buy-item';
  const input=document.createElement('input');input.type='checkbox';input.dataset.buy=id;input.checked=purchased.includes(id);
  const text=document.createElement('span');const title=document.createElement('strong');title.textContent=name;
  const meta=document.createElement('span');meta.className='buy-meta';meta.textContent=`${quantity} · ${stage}`;
  const details=document.createElement('span');details.className='buy-note';details.textContent=note;
  text.append(title,meta,details);label.append(input,text);li.append(label);list.append(li);
  input.addEventListener('change',()=>{purchased=purchased.filter(x=>x!==id);if(input.checked)purchased.push(id);try{localStorage.setItem(buyKey,JSON.stringify(purchased));}catch{buyStatus.textContent='Could not save purchases locally. Print a copy before leaving.';}updateBuyCount();});
 }
 group.append(list);buyGroups.append(group);
}
function updateBuyCount(){document.getElementById('buy-count').textContent=`${purchased.length} / ${allIds.size} items on hand`;}
updateBuyCount();
