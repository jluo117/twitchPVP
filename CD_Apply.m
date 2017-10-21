%applies cooldowns

run('Chat_Gen')
cdh=10; cdc=5; old=s;
for a=1:length(s)
    if strcmp(s(x),'heal')==1
        for i=x+1:x+cdh
            if strcmp(s(i),'heal')==1
                s{i}='delay';
            end
        end
    elseif strcmp(s(x),'counter')==1
        for j=y:y+cdc
            if strcmp(s(j),'counter')==1
                s{j}='delay';
            end
        end
    end
end
               
           
               