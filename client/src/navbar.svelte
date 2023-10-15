<script>
    const links = ['Home ', 'About '];

    import Home from "./home.svelte"
    import About from "./about.svelte"
    export let menu = 1;

</script>

<style>

nav {
        background-color: #333;
        color: white;
        height: 60px;
    }

a {
    color: white;
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

 {#if menu === 1}
            <Home />
        {:else if menu === 2}
            <About />
        {:else}
            <h1>
	            Page Not Found
            </h1>
{/if}