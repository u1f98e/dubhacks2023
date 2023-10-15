<script>
    import { onMount } from "svelte";

    let thing = 0;
    function changething()
   {
        thing = 1;
   }
   function inc2()
   {
     thing = 2;
   }
   function inc3()
   {
    thing = 3;
   }
   function decthing()
   {
        thing = 0;
   }

   let recipes = [];
   onMount(async function() {
        let response = await fetch("/api/recipe");
        recipes = await response.json();
   })
    
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
    <button on:click = {inc2}>
    <div class = "box">
        Gordon Freeman<br>
        I enjoy exotic food<br>
        3141,1245,2122<br>
    </div>
    </button>
    <button on:click = {inc3}>
    <div class = "box">
        Hannibal Lectre<br>
        I want something that pairs with a nice kiante<br>
        3113,1392,1120
    </div>
    </button>

</div>
<div class="recipeList">
{#each recipes as recipe}
    <div class = "box recipe">
        {recipe.name}<br>
        {recipe.description}<br>
    </div>
{/each}
</div>

{#if thing == 1}
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
{:else if thing == 2}
        <button on:click={decthing}>
        <p>
            Recipe: Steamed Headcrab<br>
            Id: 3141 <br>
            Description: A Headcrab steamed to draw out its natural flavor. <br>
            Ingredients: Headcrab, steamer, water, steamer, seasoning(optional) <br>
            Instructions: <br>
            Fill bottom portion of steamer with water. <br>
            Place Headcrab into top portion of steamer. <br>
            Steam for 2-4 hours or until Headcrab exterior is soft. <br>
            Apply seasonings (optional). <br>
        </p>
        </button>
{:else if thing == 3}
        <button on:click={decthing}>
            <p>
                Recipe: Lamb Liver <br>
                Id: 3113 <br>
                Description: A young lamb's liver. <br>
                Ingredients: liver <br>
                Instructions: <br>
                Best served raw. <br>
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
    p{
        color:red;
        font-family:'Wide Latin';
    }
</style>