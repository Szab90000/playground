class Team:
    def __init__(self, name, project, position):
        self.name = name
        self.proj = project
        self.pos = position
        print("-- Developer létrehozva. --")
        
    def __str__(self):
         return(f"{self.name} a {self.proj}-en dolgozik {self.pos} szerepkörben")
    
    def __eq__(self, another):
        return self.proj == another.proj

def Teammates():
    
    people = []    
    member1 = Team("Ricsi", "SolArch", "Frontend")
    print(member1)
    people.append(member1)
    member2 = Team("Angéla", "ZergTeng", "Tesztelő")
    people.append(member2) 
    print(member2)
    member3 = Team("Peti", "KefERP", "Backend")
    people.append(member3) 
    print(member3)
    member4 = Team("Éva", "KefERP", "Frontend")
    people.append(member4) 
    print(member4)
    
    return people



def Sameteam(list):
    print()
    projects = {"": []}
    for teammate in list:
        if teammate.proj in projects:
            projects[teammate.proj].append(teammate.name) 
        else:
            projects.update({teammate.proj: [teammate.name]})
    
    for team in projects:
        if(len(projects[team]) > 1):
            print(" és ".join(projects[team]) + " dolgoznak egy projekten")

 # a feladatban lévő példát egyszerűbben is meg tudnám írni, de így akkor is kijön szépen ha 2-nél többen vannak egy teamben       
 
Sameteam(Teammates())
