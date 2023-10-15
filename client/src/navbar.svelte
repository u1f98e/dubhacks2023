<script>
    const links = ['Home ', 'About '];

    import Home from "./home.svelte"
    import About from "./about.svelte"
    export let menu = 1;
</script>

<div class="header-container">
    <div class="title">Recipe Maker</div>
        <ul class="menu">
                <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li>  
                <li><a href="/" on:click|preventDefault={() => (menu = 2)}>About</a></li>
        </ul>
</div>

 {#if menu === 1}
            <Home />
        {:else if menu === 2}
            <About />
        {:else}
            <h1>
	            Page Not Found
            </h1>
{/if}

<style>
    .header-container {
        background-color: #333;
        color: white;
        height: 70px;
    }

    .title {
        padding: 10px;
        font-size: 40px;
        font-family: 'Lora';
        font-weight: 250;
    }

    .menu {
        list-style: none;
        display: flex;
    }

    .menu li {
        display: inline;
    }

    .menu a {
        text-decoration: none;
        color: orange;
        text-align: right;
    }

</style>