var actualwidth=80; //initial width of the image
var adjustwidth=60; //after enlarge image adjust the other images width
var endwidth=320; //end width of the image
var tt; //timer
var delay=100; //speed 
var arr=new Array("img1","img2","img3","img4","img5");  
var arr1=new Array(); 

Array.prototype.inArray = function (value)
{
// Returns true if the passed value is found in the
// array. Returns false if it is not.
var i;
for (i=0; i < this.length; i++) 
{
        if (this[i] == value) 
        {
        return true;
        }
}
return false;
};

function enlargeimg(iid)
{ 
      arr1.splice(0,arr1.length); 
      actualwidth=actualwidth+60;
      if(actualwidth < endwidth)    //check with end width
      {  
        for(var i=1;i<=arr.length;i++)
        {
          if(arr[i]==iid) {      
 
          }
         else
         {
            if(arr.inArray(arr[i]))
                arr1.push(arr[i]);
         }
         }    
          document.getElementById(iid).style.width=actualwidth+"px";
          for(var i=0;i<arr1.length;i++)
          {
             document.getElementById(arr1[i]).style.width=adjustwidth+"px";
          }
          tt=setTimeout("enlargeimg('"+iid+"')",delay);
       }

       if(actualwidth > endwidth) //check with end width
       {
         actualimg();
       }
 }
function actualimg()
{
     clearTimeout(tt);
     actualwidth=80;
     for(var i=0;i<arr.length;i++)
     {
        document.getElementById(arr[i]).style.width=actualwidth+"px";
     }
}
function ctck()
{
    var sds = document.getElementById("dum");
    if(sds == null){alert("You are using a free package.\n You are not allowed to remove the tag.\n");}
    var sdss = document.getElementById("dumdiv");
    if(sdss == null){alert("You are using a free package.\n You are not allowed to remove the tag.\n");}
}