<script>
  //  export let count;
 
</script>

<body>
    <div class="sidenav">
         <h1>Comments</h1>
        <!-- <p>{count}</p> -->
        <input type="text" placeholder="Share your thoughts">
        <div class="buttons">
            <button class="send">CANCEL</button>
            <button class="send">SUBMIT</button>
        </div>
    </div>
 

</body>


<style>
    body {
  font-family: "Lato", sans-serif;
  background-color: antiquewhite;
}
.main{
    background-color: aquamarine;
}
.sidenav {
  height: 100%;
  width: 25%;
  position: fixed;
  z-index: 1;
  top: 0;
  right: 0;
  background-color: #FFFFFF;
  overflow-x: hidden;
  padding-top: 40px;
  padding-left: 10px;

  h1{
    display: inline;
    /* font-family: 'Franklin Gothic'; */
    font-family: Franklin Gothic Medium,Franklin Gothic,ITC Franklin Gothic,Arial,sans-serif; 
    
  }
  p{
    display: inline;
    padding-left: 30px;
    font-size: 30px;
  }
  input{
    display: block;
    margin-top: 30px;
    width: 350px;
    height: 35px;
    padding-left: 10px;
    border-radius: 5px;
    border: solid black;
    
  }

  .buttons{
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    padding-right: 20px;
    padding-top: 10px;
     .send{
        height: 25px;
        border-radius: 5px;
        width: 70px;
        font-family: Franklin Gothic Medium,Franklin Gothic,ITC Franklin Gothic,Arial,sans-serif; 
        font-weight: bold;
        border: solid black;
      }
      .send:hover{
        background-color: #567B94;
        color: white;
        border: transparent;
      }
  }

}


</style>