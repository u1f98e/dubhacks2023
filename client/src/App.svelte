<script>
	import Home from "./home.svelte";
	import About from "./about.svelte";
	import Navbar from "./navbar.svelte";
	import Footer from "./Footer.svelte";

</script>

<style>
	main {
		text-align: left;
		padding: 1em;
		max-width: 240px;
		margin: 0;
		padding: 0;
	}


	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<main>
	<Navbar />
	<h1> This page has some textt</h1>
	<Footer />	
</main>



