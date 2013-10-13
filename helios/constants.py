#Parameters of the cryptosystem

#NEW HELIOS PARAMS
p = 168336492790373000899770943710564741850245155131062231020658882396753916974221779864139350163603145675162017217518192051402459974022901386493982150490033547527943911656071022972326328950804666984624071829398282339821044336169123550599258041247878759980349875983409102024709547196327133720478317250981146539627L
q= 84168246395186500449885471855282370925122577565531115510329441198376958487110889932069675081801572837581008608759096025701229987011450693246991075245016773763971955828035511486163164475402333492312035914699141169910522168084561775299629020623939379990174937991704551012354773598163566860239158625490573269813L
g= 45315181387564396468333986216932822394371012043143547261840922752588502031962722472636370152973566890357740909106981098033228452539319658670560307039561306236039109372619114612141519531128929920472746056084341562871789869093908251376934099746947743768816193829049261126632430965422637754104221208257819369317L

#OLD HELIOS PARAMS (NOT SAFE PRIME???)
#p = 16328632084933010002384055033805457329601614771185955389739167309086214800406465799038583634953752941675645562182498120750264980492381375579367675648771293800310370964745767014243638518442553823973482995267304044326777047662957480269391322789378384619428596446446984694306187644767462460965622580087564339212631775817895958409016676398975671266179637898557687317076177218843233150695157881061257053019133078545928983562221396313169622475509818442661047018436264806901023966236718367204710755935899013750306107738002364137917426595737403871114187750804346564731250609196846638183903982387884578266136503697493474682071L
#q = 61329566248342901292543872769978950870633559608669337131139375508370458778917L
#ground_1 and ground_2 must be in the subgroup of p generated by q => pow(ground_1,q,p) == 1
ground_1= 59442270591085997526500668610589701197635988588745410932950672513358819222909590751038673149586890941483394605463413803850272530383549203443779865590845160443166586043708141179686576610974377847126119824157047141612899922723132475177310896095298760567300170463229117605833432848788106872639333763758249940725L
ground_2= 49708428827310366368787091428000198732110042658396481412588886100233550733598450107713260356187852286541210125063981306788423921461186610835135190814212150818950911913277589202190734567289506393561034997388920101088232811771742996393829422562401288366193703145876035881882040951713756988505214096849013301257L


#Paths to private usb and local
#PATH_TO_USB = '/media/robbert/38B9-8B60/mpc/party_'
PATH_TO_USB = 'party_'
PATH_TO_LOCAL= ''

#Total number of trustees
#n=3

#Critical number of trustees to regenerate the total secret
#k=2

#keylength
n_bits = 1024
