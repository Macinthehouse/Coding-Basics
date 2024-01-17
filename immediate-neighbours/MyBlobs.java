import java.util.Deque;
import java.util.ArrayDeque;

/* -----------------------------------------
   Note: The ArrayDeque is an implementation 
         of the Deque ADT. That is, it is a 
		   double-ended queue. 

		   You can simulate both a Stack and 
		   a regular Queue with this data structure
		   in the following way:

		 Stack: push  ~ addFirst
		        pop   ~ removeFirst
		
		 Queue: enqueue ~ addLast
		        dequeue ~ removeFirst
  ------------------------------------------ */

public class MyBlobs extends Blobs{

	int index = -1;


	///////////////////////////////////////////////////////////////////////	
	///////////////////////////////////////////////////////////////////////	
	// do NOT change or remove this constructor. We will use it to create 
	// objects when testing your code. If it is removed, we cannot test 
	// your code!
	///////////////////////////////////////////////////////////////////////	
	public MyBlobs(){}
	///////////////////////////////////////////////////////////////////////	
	///////////////////////////////////////////////////////////////////////	

	public MyBlobs(Image image){
		this.image = image;
	}

	public void blobRecursiveHelper(int row, int col, Deque<Pixel> blobSoFar){

		if (row < 0 || row >= image.rows || col < 0 || col >= image.cols) {
            // pixel is out of bounds
            return;
        }

        Pixel pixel = image.getPixel(row, col);

        if (!pixel.hasInk || pixel.visited) {
            // pixel does not have ink or has been visited before
            return;
        }

        // add current pixel to blobSoFar deque and mark as visited
        blobSoFar.addLast(pixel);
        pixel.visited = true;

		// recursively visits all 4 of this pixel's immediate neighbors
		blobRecursiveHelper(row-1, col  , blobSoFar); // up
		blobRecursiveHelper(row  , col+1, blobSoFar); // right
		blobRecursiveHelper(row+1, col  , blobSoFar); // down
		blobRecursiveHelper(row  , col-1, blobSoFar); // left
}

	// this is the iterative method that you need to override
	public Deque<Pixel> blobIterative(int start_row, int start_col){
		Deque<Pixel> blobList = new ArrayDeque<Pixel>();
		Deque<Pixel> workingList = new ArrayDeque<Pixel>();

		// adds the initial pixel to workingList
		workingList.addFirst(image.getPixel(start_row, start_col));

		while(workingList.size() != 0){
			Pixel p = workingList.removeFirst();

			// checks if p has ink and has it been visited
			if(p.hasInk() && !p.visited()){
				p.setVisited(true);
				blobList.addLast(p);

				// checks if p's imediate neightbors are within the image and adds them if they are
				if(p.getRow()-1 >= 0){
					workingList.addLast(image.getPixel(p.getRow() - 1, p.getCol()    )); // up
				}
				if( p.getRow()+1 < image.rows){
					workingList.addLast(image.getPixel(p.getRow() + 1, p.getCol()    )); // down
				}
				if(p.getCol()-1 >= 0){
					workingList.addLast(image.getPixel(p.getRow()    , p.getCol() - 1)); // left
				}
				if( p.getCol()+1 < image.cols){
					workingList.addLast(image.getPixel(p.getRow()    , p.getCol() + 1)); // right
				}

			}
		}

		return blobList;
	}

}
