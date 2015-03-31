# parameters of the crypto system
p = 22454654424582173652275448964155824830479740425813270442284386576049420447533218915594779221235148116855827922121412450021652313909246475096258444304894386997164175657327993373982181887538138499835479982230585716475608651625216165510117579070901772520436399475427183909151457043285315048968393222706609755997250700932029721362854788629375380764508643679179165004939199030112976503050071103706030748475149454954016825735594117975642811819923229005930133926188134426380275962615828642816435065013401756714925699935841434454693243987919915278647225541741323860479260329434094346200744638098020616544336193256653651472887L
q = 11227327212291086826137724482077912415239870212906635221142193288024710223766609457797389610617574058427913961060706225010826156954623237548129222152447193498582087828663996686991090943769069249917739991115292858237804325812608082755058789535450886260218199737713591954575728521642657524484196611353304877998625350466014860681427394314687690382254321839589582502469599515056488251525035551853015374237574727477008412867797058987821405909961614502965066963094067213190137981307914321408217532506700878357462849967920717227346621993959957639323612770870661930239630164717047173100372319049010308272168096628326825736443L
g = 8178733718032178701037804382165280499675763604758795756159441545951169051845424837000070147681583345652694484459891984471149337625587695149098330882095225247941742912162143684887198392323521133830489528812394911770915340604363696768976015850003690470601106968419025199698290423963866741617355943081828916763488917060936883986088493018449750985272235234902956740280909299500439954027086474178410422059012795758996496109349293455061216651753565519143144186460372440543636994025651714328856789384386323386625371241772376998374860752990579502485904931950212791408950580730608782806891288959480534344063099112769514750168L

# the parameters ground_1 and ground_2 must be in the subgroup of p
# generated by q, so pow(ground_1,q,p) == 1
ground_1 = 15202490950144343753561074887400053387624924620588519730940910150453123455067094822772611161656485186306595266371292259355492927933967110622772590655368214787620569034700333613719889090009045447343230911698137538451430637785871347416655552545812953750380637007455352444344947745576316029337812847297898968744182698265629944313253197648809900557459838255450063737798315253619090024053468173151636815561682681640620397737008680957652374215632451357518092467608102740105469704803442635423847015840841452971729603506414706730406468216099508221371496246285207251489942001562789656639891860494243245573198563732266687997802L
ground_2 = 8141603035944880435121534553021201352502122511092791619785287602986420375942642142610631274271222453654548463262280550863497322227376637389460853362457549980847406346958876618012092001567647881068508690015121725364928649800255937457899811279717742592678522737539814235182592206345418655005376059791489255815147525094936722750155231023246248114697772400463582402645218681131713768387040082175537607709392650302388207906264546796548257558849747726410595106767038661740054245354400799422089926612645781834088520870174879274957026349228929270848550471009282460763735375581296603113824960689173993837792379375200729921219L

# key length
n_bits = 2048
