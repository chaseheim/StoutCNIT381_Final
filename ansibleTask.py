from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager

#Ansible skill function that gets called by the Webex bot's skill 'capture debut'
def ansible_skill():
    #equivalent terminal commnd: ansible-playbook -i ./inventory capture_debug.yaml
    loader = DataLoader()
    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
        module_path=None, forks=100, remote_user='xxx', private_key_file=None,
        ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
        become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)
    inventory = InventoryManager(loader=loader, sources=('./inventory',))
    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))
    pbex = PlaybookExecutor(playbooks=['./capture_debug.yaml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})
    results = pbex.run()
    #print(results)
    return results