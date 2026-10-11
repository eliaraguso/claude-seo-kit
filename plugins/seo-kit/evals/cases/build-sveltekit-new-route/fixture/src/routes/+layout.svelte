<script>
  let { children } = $props();
</script>

<header>
  <nav>
    <a href="/">Ada Novak</a>
    <a href="/#projects">Projects</a>
    <a href="mailto:hello@adanovak.example">Contact</a>
  </nav>
</header>

<main>
  {@render children()}
</main>

<footer>© Ada Novak · Web developer</footer>
