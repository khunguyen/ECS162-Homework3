<script lang="ts">
  export let count;
  export let title; 
  export let close;
  let inputGiven = ""; 
  var newComents : string[] = []; 

  function canceling(){
    inputGiven = ""; 
  }

  /**
   * @app.route("/<user_id>", methods=["GET"])
    def get_user(user_id):
      user = repo.get_user(user_id)
      return jsonify(user or {})

   */
  async function addComment(){
  try {
    const res = await fetch('/api/inputData', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        comment: inputGiven 
      })
    });
    if (res.ok){
     // newComents.push(inputGiven); 
     newComents = [...newComents, inputGiven];
      console.log("Comment added successfully");
      console.log(newComents);
    } else {
      console.error("Server responded with", res.status);
    }
  } catch (error) {
    console.error('Failed to add comment:', error);
  }
}
 
</script>

<div class="overlay" on:click={close}></div>
    <div class="sidenav">
      <h3>{title}</h3>
      <hr>
      <div class="middle">
          <h1>Comments</h1>
          <p>{count}</p>
      </div>
        <input type="text" placeholder="Share your thoughts" bind:value={inputGiven}>
        <div class="buttons">
            <button on:click={canceling} class="send">CANCEL</button>
            <button on:click={addComment} class="send">SUBMIT</button>
        </div>

        <div class="comments">
          {#each newComents as comment}
            <p>{comment}</p>
          {/each}
        </div>

    </div>
 




<style>
    /* body {
  font-family: "Lato", sans-serif;
  background-color: antiquewhite;
}
.main{
    background-color: aquamarine;
} */

  .overlay {
    height: 100%;
    width: 100%;
    z-index: 0; 
    position: fixed;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.3); 
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
  /* padding-top: 40px; */
  padding-left: 10px;


  h3{
    margin-bottom: 5px;
    font-family: Franklin Gothic Medium,Franklin Gothic,ITC Franklin Gothic,Arial,sans-serif; 
    font-size: 18px;
  }
  hr{
    padding: 0;

  }

  .middle{
    padding-top: 20px;
    h1{
      display: inline;
      font-size: 27px;
      /* font-family: 'Franklin Gothic'; */
      font-family: Franklin Gothic Medium,Franklin Gothic,ITC Franklin Gothic,Arial,sans-serif; 
    }
    p{
      display: inline;
      padding-left: 20px;
      font-size: 26px;
    }

  }
 
  input{
    display: block;
    margin-top: 10px;
    width: 350px;
    height: 35px;
    padding-left: 10px;
    border-radius: 5px;
    border: solid gray;
    
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
        border: solid gray;
      }
      .send:hover{
        background-color: #567B94;
        color: white;
        border: transparent;
      }
  }

}


</style>