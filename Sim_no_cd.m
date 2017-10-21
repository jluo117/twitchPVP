% Simulation of Twitch Raid

% This script simulates Twitch Raid using previously generated 

clearvars
run('Chat_Gen')
chat1=s;
clearvars -except chat1
run('Chat_Gen')
chat2=s; 
clearvars -except chat1 chat2 

hp1=1000; hp2=1000; dmg1=1; dmg2=1; hl1=2; hl2=2; 
x=1; y=1;
while 1==1

    if strcmp(chat1(x),'attack')==1
        hp2=hp2-dmg1;
    elseif strcmp(chat1(x),'delay')==1
        hp2=hp2+0;
    elseif strcmp(chat1(x),'heal')==1
        hp1=hp1+hl1;
    elseif strcmp(chat1(x),'counter')==1
        if strcmp(chat2(x),'att')==1
            hp1=hp1+dmg2;
        else
            hp1=hp1+0;
        end
    elseif strcmp(chat1(x),'bit')==1
        dmg1=dmg1+3; hl1=hl1+3; 
    end
    
    px1(x)=hp1;
    
    if strcmp(chat2(y),'attack')==1
        hp1=hp1-dmg2;
    elseif strcmp(chat2(y),'delay')==1
        hp1=hp1+0;
    elseif strcmp(chat2(y),'heal')==1
        hp2=hp2+hl2;
    elseif strcmp(chat2(y),'counter')==1
        if strcmp(chat1(y),'att')==1
            hp2=hp2+dmg2;
        else
        hp2=hp2+0;
        end
    elseif strcmp(chat2(y),'bit')
        dmg2=dmg2+3; hl2=hl2+3;
    end
    
    px2(y)=hp2;
    
    if hp1<=0 || hp2<=0 ||x==1000 || y==1000 
        break
    end
    x=x+1; y=y+1;
    
end

plot((1:x),px1,(1:y),px2)
        
      