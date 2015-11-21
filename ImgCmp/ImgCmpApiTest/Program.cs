using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;



namespace ImgCmpApiTest
{
    class Program
    {
        static void Main(string[] args)
        {
            ImgCmp image_comparator = new ImgCmp();
            var differences = image_comparator.CompareImages(
                @"..\..\test.images\pcb.1\CircuitBoard.jpg",
                @"..\..\test.images\pcb.1\CircuitBoard-diff.png");

            foreach(var d in differences)
            { 
                System.Console.WriteLine(ImgDiff_ToString(d));
            }
        }


        static string ImgDiff_ToString(ImgDiff diff)
        {
            String s = "{t:" + diff.top
                + " l:" + diff.left
                + " w:" + diff.width
                + " h:" + diff.height
                + " sad:" + diff.sad
                + "}";
            return s;
        }
    }
}
