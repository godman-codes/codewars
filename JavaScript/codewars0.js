// For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

// The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

// The following are some examples of how this class is used:

// var helper = new PaginationHelper(['a','b','c','d','e','f'], 4);
// helper.pageCount(); //should == 2
// helper.itemCount(); //should == 6
// helper.pageItemCount(0); //should == 4
// helper.pageItemCount(1); // last page - should == 2
// helper.pageItemCount(2); // should == -1 since the page is invalid

// // pageIndex takes an item index and returns the page that it belongs on
// helper.pageIndex(5); //should == 1 (zero based index)
// helper.pageIndex(2); //should == 0
// helper.pageIndex(20); //should == -1
// helper.pageIndex(-10); //should == -1

// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage) {
   this.itemPerPage = itemsPerPage;
   this.pages = [];
   this.collection = collection;
   let count = this.itemPerPage;
   for (let i = 0; i < this.collection.length; i += count) {
      this.pages.push(this.collection.slice(i, i + count));
   }
}

// PaginationHelper.prototype.pageDivider = function () {
//    let count = this.itemPerPage;
//    for (let i = 0; i < this.collection.length; i += count) {
//       this.pages.push(this.collection.slice(i, i + count));
//    }
// };

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function () {
   console.log(this.collection.length);
   return this.collection.length;
};

// returns the number of pages
PaginationHelper.prototype.pageCount = function () {
   console.log(this.pages.length);
   return this.pages.length;
};

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function (pageIndex) {
   console.log(pageIndex);
   console.log(this.pages[pageIndex]);
   if (this.pages[pageIndex] === undefined) return -1;
   return this.pages[pageIndex].length;
};

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function (itemIndex) {
   if (this.collection.length < 1) return -1;
   console.log(itemIndex);
   if (itemIndex === 0) return 0;
   if (itemIndex < 0 || itemIndex > this.collection.length - 1) return -1;
   let loc = itemIndex / this.itemPerPage;
   console.log(loc);
   let altloc = itemIndex % this.itemPerPage;
   console.log(altloc);
   if (altloc > 0) return Math.floor(loc);
   return loc - 1;
};
var helper = new PaginationHelper(["a", "b", "c", "d", "e", "f"], 4);
helper.pageCount(); //should == 2
helper.itemCount(); //should == 6
helper.pageItemCount(0); //should == 4
helper.pageItemCount(1); // last page - should == 2
helper.pageItemCount(2); // should == -1 since the page is invalid

// pageIndex takes an item index and returns the page that it belongs on
helper.pageIndex(5); //should == 1 (zero based index)
helper.pageIndex(2); //should == 0
helper.pageIndex(20); //should == -1
helper.pageIndex(-10); //should == -1
