<script>
    const links = ['Home ', 'About '];

    import Home from "./home.svelte"
    import About from "./about.svelte"
    export let menu = 1;
</script>

<<<<<<< HEAD
<style>
nav {
        background-color: #333;
        color: white;
        height: 45px;
        position: absolute;
        left: 0;
        width: 100%;
        margin: 0;
        padding: 0;

    }

a {
    color: white;
    size: 20px;
}

ul li {
    display : inline;
    color: white;
}
</style>

 <main>
    <nav>
        <ul id="menu">
            <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li>  
            <li><a href="/" on:click|preventDefault={() => (menu = 2)}>About</a></li>
        </ul>        
    </nav>
 </main>
=======
<div class="header-container">
    <div class="title">Recipe Maker</div>
        <ul class="menu">
                <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li>  
                <li><a href="/" on:click|preventDefault={() => (menu = 2)}>About</a></li>
        </ul>
</div>
>>>>>>> 9683b6350b4458d6261ffc567f367de29dd2ac44

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