import hashlib
import base64

# yara_template.yara
# rule base64_admin
# {
#    meta:
#       author = "Jeremy Richards"
#       description = "password hash"
#    strings:
#       <INSERT OUTPUT FROM SCRIPT HERE
#    condition:
#       any of them
# }


wordlist = ['123456','password','12345678','1234','pussy','12345','dragon','qwerty','696969','mustang','letmein','baseball','master','michael','football','shadow','monkey','abc123','pass','fuckme','6969','jordan','harley','ranger','iwantu','jennifer','hunter','fuck','2000','test','batman','trustno1','thomas','tigger','robert','access','love','buster','1234567','soccer','hockey','killer','george','sexy','andrew','charlie','superman','asshole','fuckyou','dallas','jessica','panties','pepper','1111','austin','william','daniel','golfer','summer','heather','hammer','yankees','joshua','maggie','biteme','enter','ashley','thunder','cowboy','silver','richard','fucker','orange','merlin','michelle','corvette','bigdog','cheese','matthew','121212','patrick','martin','freedom','ginger','blowjob','nicole','sparky','yellow','camaro','secret','dick','falcon','taylor','111111','131313','123123','bitch','hello','scooter','please','porsche','guitar','chelsea','black','diamond','nascar','jackson','cameron','654321','computer','amanda','wizard','xxxxxxxx','money','phoenix','mickey','bailey','knight','iceman','tigers','purple','andrea','horny','dakota','aaaaaa','player','sunshine','morgan','starwars','boomer','cowboys','edward','charles','girls','booboo','coffee','xxxxxx','bulldog','ncc1701','rabbit','peanut','john','johnny','gandalf','spanky','winter','brandy','compaq','carlos','tennis','james','mike','brandon','fender','anthony','blowme','ferrari','cookie','chicken','maverick','chicago','joseph','diablo','sexsex','hardcore','666666','willie','welcome','chris','panther','yamaha','justin','banana','driver','marine','angels','fishing','david','maddog','hooters','wilson','butthead','dennis','fucking','captain','bigdick','chester','smokey','xavier','steven','viking','snoopy','blue','eagles','winner','samantha','house','miller','flower','jack','firebird','butter','united','turtle','steelers','tiffany','zxcvbn','tomcat','golf','bond007','bear','tiger','doctor','gateway','gators','angel','junior','thx1138','porno','badboy','debbie','spider','melissa','booger','1212','flyers','fish','porn','matrix','teens','scooby','jason','walter','cumshot','boston','braves','yankee','lover','barney','victor','tucker','princess','mercedes','5150','doggie','zzzzzz','gunner','horney','bubba','2112','fred','johnson','xxxxx','tits','member','boobs','donald','bigdaddy','bronco','penis','voyager','rangers','birdie','trouble','white','topgun','bigtits','bitches','green','super','qazwsx','magic','lakers','rachel','slayer','scott','2222','asdf','video','london','7777','marlboro','srinivas','internet','action','carter','jasper','monster','teresa','jeremy','11111111','bill','crystal','peter','pussies','cock','beer','rocket','theman','oliver','prince','beach','amateur','7777777','muffin','redsox','star','testing','shannon','murphy','frank','hannah','dave','eagle1','11111','mother','nathan','raiders','steve','forever','angela','viper','ou812','jake','lovers','suckit','gregory','buddy','whatever','young','nicholas','lucky','helpme','jackie','monica','midnight','college','baby','cunt','brian','mark','startrek','sierra','leather','232323','4444','beavis','bigcock','happy','sophie','ladies','naughty','giants','booty','blonde','fucked','golden','0','fire','sandra','pookie','packers','einstein','dolphins','0','chevy','winston','warrior','sammy','slut','8675309','zxcvbnm','nipples','power','victoria','asdfgh','vagina','toyota','travis','hotdog','paris','rock','xxxx','extreme','redskins','erotic','dirty','ford','freddy','arsenal','access14','wolf','nipple','iloveyou','alex','florida','eric','legend','movie','success','rosebud','jaguar','great','cool','cooper','1313','scorpio','mountain','madison','987654','brazil','lauren','japan','naked','squirt','stars','apple','alexis','aaaa','bonnie','peaches','jasmine','kevin','matt','qwertyui','danielle','beaver','4321','4128','runner','swimming','dolphin','gordon','casper','stupid','shit','saturn','gemini','apples','august','3333','canada','blazer','cumming','hunting','kitty','rainbow','112233','arthur','cream','calvin','shaved','surfer','samson','kelly','paul','mine','king','racing','5555','eagle','hentai','newyork','little','redwings','smith','sticky','cocacola','animal','broncos','private','skippy','marvin','blondes','enjoy','girl','apollo','parker','qwert','time','sydney','women','voodoo','magnum','juice','abgrtyu','777777','dreams','maxwell','music','rush2112','russia','scorpion','rebecca','tester','mistress','phantom','billy','6666','albert']

#print hashlib.algorithms_available

for word in wordlist:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    md5.update(word)
    sha1.update(word)
    sha256.update(word)
    sha512.update(word)    
    #print md5.hexdigest()
    print "$"+word+"_MD5 = \"" + md5.hexdigest() + "\""
    print "$"+word+"_SHA1 = \"" + sha1.hexdigest() + "\""
    print "$"+word+"_SHA256 = \"" + sha256.hexdigest() + "\""
    print "$"+word+"_SHA512 = \"" + sha512.hexdigest() + "\""
    print "$"+word+"_BASE64 = \"" + base64.b64encode(word) + "\""
