<script>
    const links = ['Home ', 'About '];

    import Home from "./home.svelte"
    import About from "./about.svelte"
    import RecipeMaker from "./recipeMaker.svelte"
    export let menu = 1;
</script>

<div class="header-container">
    <div align="left" class="title"> Recipe Maker </div>
    <div align = "right" class="titular"></div>
        <ul class="menu">
                <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a> | </li>
                <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Create Recipe</a> | </li>
                <li><a href="/" on:click|preventDefault={() => (menu = 3)}>&nbsp;About</a></li>
        </ul>
</div>


 {#if menu === 1}
            <Home />
        {:else if menu === 2}
            <RecipeMaker />
        {:else if menu === 3}
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

    .header-container > div {
        display: inline-block;
        vertical-align: middle;
    }

    .title {
        font-family: 'Helvetica';
        justify-content: left;
        font-size: 34px;
        padding: 10px;
    }

    .menu {
        list-style: none;
        display: flex;
        justify-content: right;
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