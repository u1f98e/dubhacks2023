<script>
    import Home from "./home.svelte";
	import About from "./about.svelte";
    
    export let menu=1;
</script>

<style>


ul#menu li {
    display : inline;
}
</style>

<ul id="menu">
    <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li> |
    <li><a href="/" on:click|preventDefault={() => (menu = 2)}>About</a></li>
</ul>

{#if menu === 1}
<Home />
{:else if menu === 2}
<About />
{:else}
<h1>
    Page Not Found
</h1>
{/if}