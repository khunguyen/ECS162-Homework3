<script lang="ts">
  export let count;
  export let title; 
  export let close;
  export let idComment : number;
  let inputGiven = ""; 

  let userEmail = null;
  const modEmail = 'moderator@hw3.com';
  let modPriveleges = false;

  onMount(async () => {
    if (window.location.pathname.startsWith('/loggedIn/')) {
      const pathComponents = window.location.pathname.split('/');
      //LLM helped me with understanding how decodeURIComponent worked and was the best option to split the pathname into separate parts
      userEmail = decodeURIComponent(pathComponents[2]);
      if(userEmail === modEmail){
        modPriveleges = true;
      }
      console.log("The email (SIDEBAR): ",  userEmail, " with access of: ", modPriveleges);
    } else {
  }
  });

  // gpt helped me understand the struture of this more 
 type comment = {
    _id: string;
    comment:string;
 };
  var newComents : comment[] = []; 
   import { onMount } from 'svelte';
   // this will make the comments show up as soon as you open the side bar instead of when you click submit
  onMount(() => {
    getComment();
  });
  
  // From mongo being able to keep the comments even if they have been refreshed or close the side bar works now :DDDD
  async function getComment() {
    try {
      const res = await fetch(`/api/comments/${idComment}`); // basically get the stuff inside the comments section of the database 
      if (res.ok) {
        newComents = await res.json(); // add the list of comments to this 
      } else {
        console.error("Failed to load comments:", res.status);
      }
    } catch (error) {
      console.error("Error loading comments:", error);
    }
  }

  async function addComment(){
    try {
      const res = await fetch(`/api/inputData/${idComment}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          comment: inputGiven 
        })
      });
      if (res.ok){
      // newComents.push(inputGiven); 
      //newComents = [...newComents, inputGiven];
      await getComment();
        console.log("Comment added successfully");
        console.log(newComents);
      } else {
        console.error("Server responded with", res.status);
      }
    } catch (error) {
      console.error('Failed to add comment:', error);
    }
}

  function canceling(){
    inputGiven = ""; 
  }

  async function deleteComment(object_ID: string){
    try {
      const res = await fetch(`/api/InputData/DeleteComment/${object_ID}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' }
      });
      if (res.ok){
        await getComment();
        console.log("Successfully deleted comment");
      } else {
        console.error("Server responded with", res.status);
      }
    } catch (error) {
      console.error('Failed to delete comment:', error);
    }
  }

  async function replyComment(object_ID : string){

  }

 
</script>
<!-- makes it look better -->
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
            <p>{comment.comment}</p>
            {#if modPriveleges}
              <button on:click={() => deleteComment(comment._id)}>Delete</button>
            {/if}
            <button>Reply</button>
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

  .comments{
    display:grid
    
  }

}


</style>