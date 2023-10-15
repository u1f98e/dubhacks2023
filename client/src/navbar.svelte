<script>
    const links = ['Home ', 'About '];
</script>

<style>

nav {
        background-color: #333;
        color: white;
    }

ul li {
    display : inline;
}

</style>

 <main>
    <nav>
        <ul>
            {#each links as link}
                <li on:click={() => handleClick(link)}>{link}</li>
            {/each}
        </ul>
    </nav>
 </main>