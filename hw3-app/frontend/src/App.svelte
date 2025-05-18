<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from './lib/sidebar.svelte';

  const date = new Date();
  const options: Intl.DateTimeFormatOptions = {
      weekday: "long",
      month: 'long',
      day: 'numeric',
      year: 'numeric'     
  };
  const current_date: string = date.toLocaleDateString(undefined, options);

  let apiKey: string = '';
  
  let firstColumn: any[] = [];
  let secondColumn: any[] = [];
  let thirdColumn: any[] = [];


    let firstColumn0_1_image: string = '';
    let firstColumn0_1_headline: string = '';
    let firstColumn0_1_snippet: string = '';


    let firstColumn0_2_image: string = '';
    let firstColumn0_2_headline: string = '';
    let firstColumn0_2_snippet: string = '';


    let secondCol0_1_headline: string = '';
    let secondCol0_1_image: string = '';
    let secondCol0_1_snippet: string = '';


    let secondCol0_2_headline: string = '';
    let secondCol0_2_image: string = '';
    let secondCol0_2_snippet: string = '';

    let thirdCol0_1_headline: string = '';
    let thirdCol0_1_image: string = '';
    let thirdCol0_1_snippet: string = '';
    
    let thirdCol0_2_headline: string = '';
    let thirdCol0_2_image: string = '';
    let thirdCol0_2_snippet: string = '';

 let loginButtonName;

  if (window.location.pathname === '/loggedIn') {
    loginButtonName = "Account";
  } else {
    loginButtonName = "LOG IN";
  }

  function handleLogin() {
    if (window.location.pathname !== '/loggedIn') {
      window.location.href = 'http://localhost:8000/login';
    } else {
     // NEED TO ADD THE ACOUNT STUFF HERE 
     window.location.href = 'http://localhost:8000';
     
    }
  }



  onMount(async () => {
    try {
      const res = await fetch('/api/key');
      const data = await res.json();
      apiKey = data.apiKey;
      console.log("Initiating apiKey...", apiKey);
    } catch (error) {
      console.error('Failed to fetch API key:', error);
    }  
    
    console.log("This is the apiKey:",apiKey);
    
    var davisRequest = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q="Davis, California"&api-key=${apiKey}`
    
    let sacRequest = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q="Sacramento, California"&api-key=${apiKey}`

    let woodlandRequest = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q="UC Davis"&api-key=${apiKey}`

    let url = window.location.href;
    console.log(url);

    fetch(davisRequest)
      .then(response => response.json())
      .then(data => {
        //Retrieves data from NYT API and places array of responses in firstColumn
        firstColumn = data.response.docs;
        console.log(firstColumn);
        
        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        firstColumn0_1_headline = firstColumn[1].headline.main;
        firstColumn0_1_snippet = firstColumn[1].snippet;
        firstColumn0_1_image = firstColumn[1].multimedia.default.url;

        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        firstColumn0_2_headline = firstColumn[4].headline.main;
        firstColumn0_2_snippet = firstColumn[4].snippet;
        firstColumn0_2_image = firstColumn[4].multimedia.default.url;

      })
      .catch(error => {
        console.log(`Error fetching data:`, error)
      });

      fetch(sacRequest)
      .then(response => response.json())
      .then(data => {
        //Retrieves data from NYT API and places array of responses in secondColumn
        secondColumn = data.response.docs;

        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        secondCol0_1_headline = secondColumn[1].headline.main;
        secondCol0_1_snippet = secondColumn[1].snippet;
        secondCol0_1_image = secondColumn[1].multimedia.default.url;
        
        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        secondCol0_2_headline = secondColumn[2].headline.main;
        secondCol0_2_snippet = secondColumn[2].snippet;
        secondCol0_2_image = secondColumn[2].multimedia.default.url;
      })
      .catch(error => {
        console.log(`Error fetching data:`, error)
      });

      fetch(woodlandRequest)
      .then(response => response.json())
      .then(data => {
        //Retrieves data from NYT API and places array of responses in thirdColumn
        thirdColumn = data.response.docs;

        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        thirdCol0_1_headline = thirdColumn[1].headline.main;
        thirdCol0_1_snippet = thirdColumn[1].snippet;
        thirdCol0_1_image = thirdColumn[1].multimedia.default.url;
        
        //Places random element from the response array and retrieves the headline, snippet, and url to the article image [all are string as cast in the lines above]
        thirdCol0_2_headline = thirdColumn[2].headline.main;
        thirdCol0_2_snippet = thirdColumn[2].snippet;
        thirdCol0_2_image = thirdColumn[2].multimedia.default.url;
      })
      .catch(error => {
        console.log(`Error fetching data:`, error)
      });
  });


let sidebar = false; 
let buttonCount :number[]= [108, 123, 234, 23, 42]; 
let counting = 0; 
let mainTile = "";
  function toggleBar(count :number, title: string) {
    sidebar = true; // !sidebar;
   counting = count; 
   mainTile = title; 
   // document.getElementById("mainy").style.backgroundColor = "#5A5A5A";
  }
  function closeBar(){
    sidebar = false; 
  }

async function addComment(){
  try {
    const res = await fetch('/api/inputData', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        comment: "This is a test comment" 
      })
    });
    if (res.ok){
      console.log("Comment added successfully");
    } else {
      console.error("Server responded with", res.status);
    }
  } catch (error) {
    console.error('Failed to add comment:', error);
  }
}
</script>


<svelte:head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <title>The New York Times
    </title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</svelte:head>

<main id="mainy">
    <div class="nav_bar">
        <!-- <button id="search"><i class="fa fa-search"></i></button> -->
        
        <!-- <div class="language">
            <a href="https://www.nytimes.com/">U.S.</a> 
            <a href="https://www.nytimes.com/international/">INTERNATIONAL</a>
            <a href="https://www.nytimes.com/ca/">CANADA</a>
            <a href="https://www.nytimes.com/es/">ESPAÑOL</a>
            <a href="https://cn.nytimes.com/">中文</a>
        </div>

        <button id="subscribe"><strong>SUBSCRIBE FOR $1/WEEK</strong></button> -->
        <!-- <button on:click= {handleLogin} id="account" >Login</button> -->

    </div>
    
    <div class="header">
      <button on:click= {handleLogin} class={loginButtonName === "LOG IN" ? "login" : "account"}>{loginButtonName}</button>
        <p id="currentDate" data-testid="current-date">{current_date}</p>
        <p>Today's Paper</p>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/NewYorkTimes.svg/1280px-NewYorkTimes.svg.png" alt="The New York Times Logo" id="nyt-logo">
         

    </div>

    <!-- <div class="for-border"></div> -->
    
    <div class="topics">
        <ul>
            <li>U.S.</li>
            <li>World</li>
            <li>Business</li>
            <li>Arts</li>
            <li><a href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0vN_ZgsYoL1wl9pFC9wf03VbTiTlGVwVkdBL4io10VqobwYad4XDBlgRom_s6uoRojVw&usqp=CAU">Lifestyle</a></li>
            <li>Opinion</li>

            <li>Audio</li>
            <li>Games</li>
            <li>Cooking</li>
            <li><a href="https://image.petmd.com/files/inline-images/munchkin-kitten.jpg?VersionId=UGxw_dIhR8YTATWyXOmDRvicUNhY6dXs">Cats</a></li>
            <li>The Lazy</li>
        </ul>
    </div>
    <hr class="bold">
    <hr class="bold">

    <div class="grid-container">

        <div class="article" id="item1">

          <div class="title" id="title3">{firstColumn0_1_headline}</div>

          <img src={firstColumn0_1_image} alt="alt">

          <p>{firstColumn0_1_snippet}</p>
          <button on:click={addComment}>CLICK THIS</button>
        
          <button on:click={() => toggleBar(buttonCount[0], firstColumn0_1_headline)}><i class="fa-solid fa-message"></i>{buttonCount[0]}</button>
         

        </div>

        <div class="article" id="item2">

          <div class="title" id="title3">{secondCol0_1_headline}</div>
            
          <img src={secondCol0_1_image} alt="alt">
          
          <p>{secondCol0_1_snippet}</p>  
           <button on:click={() => toggleBar(buttonCount[1], secondCol0_1_headline)}><i class="fa-solid fa-message"></i>{buttonCount[1]}</button>
         
        </div>

        <div class="article" id="item3">

          <div class="title" id="title3">{thirdCol0_1_headline}</div>
          <img src={thirdCol0_1_image} alt="alt">

          <p>{thirdCol0_1_snippet}</p>  
           <button on:click={() => toggleBar(buttonCount[2], thirdCol0_1_headline)}><i class="fa-solid fa-message"></i>{buttonCount[4]}</button>
         

        </div>

        <div class="article" id="item4">
          <div class="title" id="title3">{firstColumn0_2_headline}</div>
      
          <img src={firstColumn0_2_image} alt="alt">

          <p>{firstColumn0_2_snippet}</p>     
           <button on:click={() => toggleBar(buttonCount[3],firstColumn0_2_headline)}><i class="fa-solid fa-message"></i>{buttonCount[4]}</button>
          

      </div>

        <div class="article" id="item5">

          <div class="title" id="title3">{thirdCol0_2_headline}</div>
           
          <img src={thirdCol0_2_image} alt="alt">

          <p>{thirdCol0_2_snippet}</p>  
           <button on:click={() => toggleBar(buttonCount[4], thirdCol0_2_headline)}><i class="fa-solid fa-message"></i>{buttonCount[4]}</button>
         
           {#if sidebar}
             <Sidebar count={counting} title={mainTile} close={closeBar}></Sidebar>
          {/if}

        </div>
    </div>

    <div class="footer"></div>

</main>
