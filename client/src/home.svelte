<script>
    let thing = 0;
    function changething()
   {
        thing = thing + 1;
   }
   function decthing()
   {
        thing = thing - 1;
   }
    
</script>
<div class="recipes-title">Profiles you'd like...</div>
<div class = "container">
    <button on:click = {changething}>
        
    <div class = "box">
        Jeremy Johannson<br>
        I like spicy food.<br>
        1234,3564,2111<br>
    </div>
    </button>
    <button>
    <div class = "box">
        Gordon Freeman<br>
        I enjoy exotic food<br>
        3141,1245,2122<br>
    </div>
    </button>
    <button>
    <div class = "box">
        Hannibal Lectre<br>
        I want something that pairs with a nice kiante<br>
        3113,1392,1120
    </div>
    </button>
</div>

{#if thing > 0}
        <button on:click = {decthing}>
            <p>
                Recipe: boiled water <br>
                Id: 1234 <br>
                Description: a nice boiling cup of water. <br>
                Ingredients: pot, water, stove or other source of heat <br>
                Instructions: <br>
                Place water into pot <br> 
                Place pot on stove <br>
                Turn stove on <br>
                Wait until water starts bubbling violently <br>
            </p>
        </button>
{/if}

<style>
    .recipes-title {
        padding: 10px;
        font-size: 20px;
        font-family: 'Lora';
        font-weight: 250;
    }
    .container {
        display: flex;
        /* justify-content: space-between; */
    }
    .box {
        width: 300px;
        height: 300px;
        border: 1px solid black;
        padding: 5px;
        margin: 25px;
        text-align: center;
        font-family: 'Arial, Helvetica, sans-serif';
        color: darksalmon;
    }
</style>