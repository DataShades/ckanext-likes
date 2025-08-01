from __future__ import annotations

from typing_extensions import override

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.common import CKANConfig


@tk.blanket.actions
@tk.blanket.auth_functions
@tk.blanket.blueprints
@tk.blanket.cli
@tk.blanket.config_declarations
@tk.blanket.helpers
class LikesPlugin(
    p.IConfigurer,
    p.SingletonPlugin,
):
    @override
    def update_config(self, config: CKANConfig):
        tk.add_template_directory(config, "templates")
