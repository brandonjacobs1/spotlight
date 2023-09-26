# spotlight_filters.py

from django import template

register = template.Library()


@register.filter
def format_spotlights(spotlights):
    formatted_spotlights = []
    link = "{% url 'edit' spotlight.id%}"
    for spotlight in spotlights:
        formatted_spotlight = f"""
        <div class="col">
            <div class="card" style="width: 18rem;">
                <img src="{spotlight.image.url}" class="card-img-top" alt="{spotlight.last_name}">
                <div class="card-body">
                    <h5 class="card-title">{spotlight.first_name_husband} and {spotlight.first_name_wife} {spotlight.last_name}</h5>
                        <p class="card-text text-truncate">{spotlight.bio}</p>
                        <a href={link} class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>
        """
        formatted_spotlights.append(formatted_spotlight)
    return "\n".join(formatted_spotlights)
