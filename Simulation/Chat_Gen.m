% Twitch Raid mock chat generator 

% This script generates a cell of n=10000 entries of strings labeled
% as attack, counter, heal, bit, or delay
x=0; y=0;
n=10000;
for a=1:n
    x(a)=ceil(rand*1000);
    y(a)=ceil(rand*1000);
end

i=(x+y)*5;

hel=find(i<1000); 
del=find(i<6500 & i>1000);
att=find(i>6500 & i<8000);
cnt=find(i>8000 & i<9500);
bit=find(i>9500);


for c=1:n
    s{c}={};
end

for b=bit
    s{b}='bit';
end

for h=hel
    s{h}='heal';
end

for a=att
s{a}='attack';
end

for d=del
    s{d}='delay';
end

for c=cnt
s{c}='counter';
end

%^ Produces a test twitch stream chat


