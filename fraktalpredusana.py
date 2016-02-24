import math,sys
from PIL import ImageDraw,Image
 
 
def frak(d,n,p):
    if (n<=0): return;
    hrany=len(p)
    stred=[]
   
    for i in range(0,hrany):
			 l_center = ( (p[(i-1)%hrany][0]+p[i][0])/2 ,(p[(i-1)%hrany][1]+p[i][1])/2 ) #najdi stred vlavo
			 r_center = ( (p[(i+1)%hrany][0]+p[i][0])/2 ,(p[(i+1)%hrany][1]+p[i][1])/2 ) #najdi stred vpravo
			 
			 #potiahni normalovy vektor z laveho stredu
			 l_inter  = ( l_center[0] + ( l_center[1]-p[i][1] ) , l_center[1] + (-1)*(l_center[0]-p[i][0]) )
			 
			 #potiahni normalovy vektor z praveho stredu
			 r_inter  = ( r_center[0] + (-1)*( r_center[1]-p[i][1] ) , r_center[1] + (r_center[0]-p[i][0]) )
			 
			 #zbieraj stredove body na postavenie stredoveho k-uholnika
			 stred.append(l_inter)
			 
			 #potiahni kolmicu z laveho stredu (bude to robit z kazdeho rohu takze by mal obehnut kazdu hranu)
			 d.line( (l_center[0],l_center[1],l_inter[0],l_inter[1]) )
			 
			 #pre kazdy 5 uholnik pusti znovu tento alg
			 
			 frak(d,n-1,[r_center,r_inter,l_inter,l_center,p[i]])
   
    #nakresli stredovy k-uholnik
    for i in range(0,len(stred)):
        d.line((stred[i][0],stred[i][1],stred[(i+1)%len(stred)][0],stred[(i+1)%len(stred)][1]))
   
    #pusti frak na stredovy k-uholnik
    frak(d,n-1,stred)
       
def generate_uholnik(x,y,r,n): #x,y su stred, r je vzdialenost |stred vrchol|, n je pocet stran
    uholnik=[]
    for i in range(0,n):
        uholnik.append( ( x+math.cos(i*math.radians(72))*r , y+math.sin(i*math.radians(72))*r ) )
    return uholnik
 
 
 
def main():
    dimensions = (3200, 3200)

    p=generate_uholnik(dimensions[0]/2,dimensions[1]/2,min(dimensions)/2-100,5)      
    #print len(p)
 
    img = Image.new("RGB", dimensions)
    d = ImageDraw.Draw(img)
    for i in range(0,len(p)):
        
        d.line((p[i][0],p[i][1],p[(i+1)%5][0],p[(i+1)%5][1]))
 
    frak(d,6,p)
   
   
    del d
    img.save("result.png")
    
main()
