        self.activated_abilities = []
        self.triggered_abilities = []
        self.passive_abilities   = []
        self.keyword_abilities   = []

        for ability in self._activated_abilities.split('\n'):

            if ability := ability.strip():
                if '||' in ability:
                    self.activated_abilities.append(ability.split('||'))
                else:
                    self.activated_abilities.append(['', ability])

        for ability in self._triggered_abilities.split('\n'):

            if ability := ability.strip():
                if '||' in ability:
                    self.triggered_abilities.append(ability.split('||'))
                else:
                    self.triggered_abilities.append(['', ability])

        for ability in self._keyword_abilities.split('\n'):

            if ability := ability.strip():
                if '||' in ability:
                    self.keyword_abilities.append(ability.split('||'))
                else:
                    self.keyword_abilities.append(['', ability])

        for ability in self._passive_abilities.split('\n'):

            if ability := ability.strip():
                if '||' in ability:
                    self.passive_abilities.append(ability.split('||'))
                else:
                    self.passive_abilities.append(['', ability])