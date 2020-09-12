
def queue_battle(dist,*armies):
    """
    https://www.codewars.com/kata/5d617c2fa5e6a2001a369da2
    4 kyu
    
    This version contains print statements which essentially create a battle log
    There are also example setup at the bottom that are current commented out
    """
    DIST = dist
    ARMY_COUNT = len(armies)
    
    #Keep track of active armies - needed for reassigning targets
    active_armies = []
    for army in range (0,ARMY_COUNT):
        active_armies.append(army)
    
    #Add each army and target to dictionary
    queues = {}
    for n, army in enumerate(armies):
        if n==len(armies)-1:
            target = 0
        else:
            target = n+1
        queues[n]={'target':target,'army':{k:v for k,v in enumerate(list(army))}}
        
        
    #Print Armies for testing
    print("Starting Armies")
    for army, data in queues.items():        
        print(army,data)
    
    #Declare variables for game loop
    round = 1
    bullet_count = 1
    bullets={
        #1:{'dist':0,'speed':100,'target':""},
        #2:{'dist':0,'speed':200,'target':""}
             }   
    
    #Start game loop
    no_victor = True
    while no_victor:
   
        #Print starting round
        print()
        print("ROUND",round)
        
        #Print starting armies
        print("Starting Armies")
        for army in queues:
            print("Army Index",army,queues[army]["army"])
        print()
        

        #CODE FOR BULLETS
        bullets_hit = []
        targets_hit = []

        #Check if any current bullets hit
        for bullet, data in bullets.items():
            bullets[bullet]['dist'] += bullets[bullet]['speed']
            if bullets[bullet]['dist'] >= DIST:
                bullets_hit.append(bullet)
                targets_hit.append(bullets[bullet]['target'])
        print("Targets hit in ROUND",round)
        print(targets_hit)
        
        #Remove bullets that hit
        for bullet in bullets_hit:
            bullets.pop(bullet)  
            
        #Fire off new bullets
        armies_to_be_removed = []
        for army in queues:
            #find first key
            fk = list(queues[army]['army'].keys())[0]
            if army in targets_hit:
                #Remove first soldier if hit
                queues[army]['army'].pop(fk)
                #Check if army has remaining soldiers
                if len(queues[army]['army']) == 0:
                    armies_to_be_removed.append(army)
            else:
                bullets[bullet_count]={'dist':0,'speed':queues[army]['army'][fk],'target':queues[army]['target']}
                bullet_count += 1
                #Rotate first soldier to the back
                x = queues[army]['army'][fk] 
                queues[army]['army'].pop(fk)
                queues[army]['army'][fk]=x
                
        #Remove current bullets if elimination occurs.        
        if len(armies_to_be_removed) > 0:
            bullets={}
              
        #Updates active_armies list
        for army in armies_to_be_removed:
            active_armies.remove(army)
            queues.pop(army)
            
        #Assign new targets
        for army in queues:
            if queues[army]['target'] not in active_armies:
                new_target=active_armies.index(army)+1
                if new_target > len(active_armies)-1:
                    new_target=0
                queues[army]['target']=active_armies[new_target]
                
        print("Active bullets end of round",round)
        for bullet, data in bullets.items():
            print(bullet,data)
           
        #Ends loops if one or zero armies remain
        if len(queues) <= 1:
                no_victor=False
        
        round += 1
        
    print("BATTLE OVER. Remaining",active_armies)
    print("DIST was",DIST)
    
    if active_armies == []:
        
        print((-1,()))
        return (-1,())
    
    else:
        winning_army = active_armies[0]
        leftover_soldiers = list(queues[army]['army'].keys())
        return(winning_army,tuple(leftover_soldiers))
    
###############################################################################
        
# queue_battle(100,(25,38,55,46,82),(64,90,37,25,58))
# queue_battle(200,(61,83,37,55,92,35,68,72),(90,81,36,114,67,25,31,84))
# queue_battle(300,(98,112,121,95,63),(120,94,90,88,30),(116,144,45,200,32))
# queue_battle(400,(186,78,56,67,78,127,78,192),(78,67,208,45,134,212,82,99),(327,160,49,246,109,98,44,57))
# queue_battle(500,(345,168,122,269,151),(56,189,404,129,101),(364,129,209,163,379),(520,224,154,74,420))
        
    
    
# ABdist = 480    
# A = (286, 68, 154, 430, 415, 360, 137, 228, 196, 575, 158, 457, 418, 298, 128, 439, 60, 425, 243, 180, 116, 51, 409, 941)
# B = (464, 68, 266, 443, 467, 76, 256, 147, 436, 249, 102, 149, 435, 365, 184, 307, 63, 409, 281, 564, 361, 462, 82, 281)
# # queue_battle(ABdist,A,B)